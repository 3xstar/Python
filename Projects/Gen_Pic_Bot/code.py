import base64
import json
import os
import time
from typing import Dict, Optional

import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)

load_dotenv()
import logging
logging.basicConfig(level=logging.INFO)

class FusionBrainAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_pipeline(self):
        response = requests.get(self.URL + 'key/api/v1/pipelines', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt: str, pipeline: str, width: int = 1024, height: int = 1024, style: str = "ANIME"):
        params = {
            "type": "GENERATE",
            "numImages": 1,
            "width": width,
            "height": height,
            "style": style,
            "generateParams": {
                "query": prompt
            }
        }

        data = {
            'pipeline_id': (None, pipeline),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/pipeline/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id: str, file_name: str = "generated_image.png", attempts: int = 10,
                         delay: int = 10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/pipeline/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()

            if data['status'] == 'DONE':
                image_data = base64.b64decode(data['result']['files'][0])
                with open(file_name, "wb") as file:
                    file.write(image_data)
                return file_name

            attempts -= 1
            time.sleep(delay)
        return None


class TelegramBot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.fusion_brain = FusionBrainAPI(
            'https://api-key.fusionbrain.ai/',
            os.getenv('FUSIONBRAIN_API_KEY'),
            os.getenv('FUSIONBRAIN_SECRET_KEY')
        )
        self.user_settings: Dict[int, Dict] = {}  # {chat_id: {style: str, width: int, height: int}}
        self.prompt_storage: Dict[str, str] = {}  # {prompt_hash: original_prompt}

    def _get_prompt_by_hash(self, prompt_hash: str) -> Optional[str]:
        return self.prompt_storage.get(prompt_hash)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.message.chat.id
        self._init_user_settings(chat_id)

        await update.message.reply_text(
            "🎨 *Бот для генерации изображений* 🎨\n\n"
            "Отправьте мне описание картинки, и я её создам!\n\n"
            "Доступные команды:\n"
            "/help - справка по использованию\n"
            "/style - выбрать стиль изображения\n"
            "/size - изменить размер изображения\n"
            "/example - примеры запросов\n\n"
            "Пример: *\"Космический кот в скафандре\"*",
            parse_mode='Markdown'
        )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "🖼️ *Помощь по боту* 🖼️\n\n"
            "Основные команды:\n"
            "/start - начать работу\n"
            "/help - эта справка\n"
            "/style - выбрать стиль (аниме, реализм и др.)\n"
            "/size - изменить размер изображения\n"
            "/example - примеры запросов\n\n"
            "Просто отправьте текстовое описание картинки, и я её сгенерирую!\n\n"
            "Сейчас установлено:\n"
            f"Стиль: {self._get_user_setting(update.message.chat.id, 'style')}\n"
            f"Размер: {self._get_user_setting(update.message.chat.id, 'width')}x{self._get_user_setting(update.message.chat.id, 'height')}"
        )
        await update.message.reply_text(help_text, parse_mode='Markdown')

    async def set_style(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        styles = {
            'ANIME': 'Аниме 🎎',
            'DEFAULT': 'Стандартный 🖼️',
            'UHD': 'Высокая детализация 🔍',
            'KANDINSKY': 'Кандинский 🎨',
            '3D': '3D-стиль 🏗️'
        }

        keyboard = [
            [InlineKeyboardButton(text, callback_data=f"style_{style}")]
            for style, text in styles.items()
        ]

        await update.message.reply_text(
            "Выберите стиль изображения:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    async def set_size(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        sizes = {
            '512x512': '512×512 (мини)',
            '768x768': '768×768 (средний)',
            '1024x1024': '1024×1024 (стандарт)',
            'custom': 'Другой размер...'
        }

        keyboard = [
            [InlineKeyboardButton(text, callback_data=f"size_{size}")]
            for size, text in sizes.items()
        ]

        await update.message.reply_text(
            "Выберите размер изображения:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    async def example(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        examples = [
            "Космический кот в скафандре",
            "Замок на облаке в стиле аниме",
            "Робот-художник рисует картину",
            "Фэнтезийный лес с светящимися растениями",
            "Киберпанк город в дожде ночью"
        ]

        await update.message.reply_text(
            "🎭 *Примеры запросов:* 🎭\n\n" +
            "\n".join(f"• `{ex}`" for ex in examples) +
            "\n\nПопробуйте изменить эти запросы или придумать свои!",
            parse_mode='Markdown'
        )

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat.id
        data = query.data

        self._init_user_settings(chat_id)

        if data.startswith("style_"):
            style = data.split("_")[1]
            self.user_settings[chat_id]['style'] = style
            await query.edit_message_text(f"✅ Стиль изменен на: {style}")

        elif data.startswith("size_"):
            size = data.split("_")[1]
            if size == 'custom':
                await query.edit_message_text("Введите размер в формате: ШИРИНА ВЫСОТА (например: 800 600)")
            else:
                w, h = map(int, size.split('x'))
                self.user_settings[chat_id]['width'] = w
                self.user_settings[chat_id]['height'] = h
                await query.edit_message_text(f"✅ Размер изменен на: {w}x{h}")

        elif data == "change_style":
            await self.set_style(update, context)

        elif data == "change_size":
            await self.set_size(update, context)

        elif data.startswith("regenerate_"):
            prompt_hash = data.split("_")[1]
            # Здесь вам нужно восстановить оригинальный промпт по хэшу
            # Это может потребовать сохранения промптов в словаре
            original_prompt = self._get_prompt_by_hash(prompt_hash)
            if original_prompt:
                await self._generate_and_send_image(update, chat_id, original_prompt)
            else:
                await query.answer("Не удалось найти оригинальный запрос")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.message.chat.id
        text = update.message.text

        # Handle custom size input
        if self._is_size_input(text):
            try:
                width, height = map(int, text.split())
                if width < 256 or height < 256 or width > 2048 or height > 2048:
                    raise ValueError

                self._init_user_settings(chat_id)
                self.user_settings[chat_id]['width'] = width
                self.user_settings[chat_id]['height'] = height

                await update.message.reply_text(f"✅ Установлен размер: {width}x{height}")
                return
            except:
                await update.message.reply_text("❌ Неверный формат. Введите два числа через пробел (например: 800 600)")
                return

        # Handle generation request
        await self._generate_and_send_image(update, chat_id, text)

    async def _generate_and_send_image(self, update: Update, chat_id: int, prompt: str):
        self._init_user_settings(chat_id)
        settings = self.user_settings[chat_id]

        # Send "Generating..." message with typing action
        await update.message.reply_text(
            f"🖌️ Генерирую изображение...\n"
            f"Стиль: {settings['style']}\n"
            f"Размер: {settings['width']}x{settings['height']}\n\n"
            "Пожалуйста, подождите ⏳"
        )

        try:
            pipeline_id = self.fusion_brain.get_pipeline()
            uuid = self.fusion_brain.generate(
                prompt=prompt,
                pipeline=pipeline_id,
                width=settings['width'],
                height=settings['height'],
                style=settings['style']
            )

            image_path = self.fusion_brain.check_generation(uuid)

            if image_path:
                with open(image_path, 'rb') as photo:
                    await update.message.reply_photo(
                        photo=photo,
                        caption=f"🎨 Результат: '{prompt}'\n"
                                f"Стиль: {settings['style']} | "
                                f"Размер: {settings['width']}x{settings['height']}"
                    )
                os.remove(image_path)
            else:
                await update.message.reply_text("❌ Не удалось сгенерировать изображение. Попробуйте позже.")

        except Exception as e:
            await update.message.reply_text(f"⚠️ Ошибка: {str(e)}")

    def _init_user_settings(self, chat_id: int):
        if chat_id not in self.user_settings:
            self.user_settings[chat_id] = {
                'style': 'ANIME',
                'width': 1024,
                'height': 1024
            }

    def _get_user_setting(self, chat_id: int, key: str):
        self._init_user_settings(chat_id)
        return self.user_settings[chat_id][key]

    def _is_size_input(self, text: str) -> bool:
        parts = text.split()
        return len(parts) == 2 and all(part.isdigit() for part in parts)

    def run(self):
        application = Application.builder().token(self.bot_token).build()

        # Command handlers
        application.add_handler(CommandHandler('start', self.start))
        application.add_handler(CommandHandler('help', self.help))
        application.add_handler(CommandHandler('style', self.set_style))
        application.add_handler(CommandHandler('size', self.set_size))
        application.add_handler(CommandHandler('example', self.example))

        # Message handlers
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Callback handlers
        application.add_handler(CallbackQueryHandler(self.handle_callback))

        application.run_polling()


if __name__ == '__main__':
    bot = TelegramBot()
    bot.run()
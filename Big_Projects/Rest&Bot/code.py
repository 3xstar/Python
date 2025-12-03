import httpx
from deep_translator import GoogleTranslator
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
    ConversationHandler
)
from yandexgptlite import YandexGPTLite
import logging
import asyncio

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Константы
SPOONACULAR_API_KEY = '86569863fa3640b4a144a7d00c7d22cb'
BOT_TOKEN = '7666993489:AAF-gXqqsEevm9i08vjGRDHYDPMGagLlivI'

# Состояния ConversationHandler
GET_RECIPES, ASK_QUESTION = range(2)

# Инициализация YandexGPT
gpt = YandexGPTLite(
    folder="b1gfkj4il6umdgmv3729",
    token="y0_AgAAAAB6kYcvAATuwQAAAAEcm1PMAABq_E9vFrtB3Y0q8TzsFhl-u1X1DA"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка приветственного сообщения с клавиатурой."""
    keyboard = [
        [
            InlineKeyboardButton("🍳 Получить рецепты", callback_data='get_recipes'),
            InlineKeyboardButton("🧠 Нейросеть", callback_data='ask_question')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "👋 Привет! Я ваш кулинарный и интеллектуальный помощник. Выберите действие:",
            reply_markup=reply_markup
        )
    else:
        await update.callback_query.message.reply_text(
            "👋 Привет! Я ваш кулинарный и интеллектуальный помощник. Выберите действие:",
            reply_markup=reply_markup
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка информации о помощи."""
    await update.message.reply_text(
        "ℹ️ *Помощь по боту:*\n\n"
        "1. *Поиск рецептов* - Нажмите кнопку 'Получить рецепты' и введите ингредиенты через запятую\n"
        "2. *Вопрос к нейросети* - Нажмите кнопку 'Нейросеть' и задайте любой вопрос\n\n"
        "Используйте /start для возврата в главное меню",
        parse_mode="Markdown"
    )


async def admin_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка информации об администраторе."""
    await update.message.reply_text(
        "👨‍💼 *Информация о разработчике:*\n\n"
        "Руководитель проекта: Соловьёв Захар Олегович\n"
        "По вопросам и предложениям:\n"
        "Telegram: @bruhlmaocringe\n"
        "Email: tmrniket@gmail.com\n\n"
        "Используйте /start для возврата в главное меню",
        parse_mode="Markdown"
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Отмена текущей операции и возврат в главное меню."""
    await update.message.reply_text("Операция отменена.")
    await show_main_menu(update.message)
    return ConversationHandler.END


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Обработка нажатий кнопок и установка состояния разговора."""
    query = update.callback_query
    await query.answer()

    try:
        if query.data == 'get_recipes':
            await query.edit_message_text(
                "🍴 Введите ингредиенты через запятую (например: яйца, молоко, мука):"
            )
            return GET_RECIPES
        elif query.data == 'ask_question':
            await query.edit_message_text(
                "💡 Задайте ваш вопрос или опишите задачу:"
            )
            return ASK_QUESTION
    except Exception as e:
        logger.error(f"Error in button_handler: {e}")
        await query.message.reply_text("❌ Произошла ошибка. Попробуйте снова.")

    return ConversationHandler.END


async def get_recipes_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Поиск рецептов с обработкой ошибок."""
    try:
        user_input = update.message.text
        if not user_input.strip():
            await update.message.reply_text("❌ Пожалуйста, укажите хотя бы один ингредиент.")
            return GET_RECIPES

        # Статусное сообщение
        status_msg = await update.message.reply_text("🔍 Ищу рецепты... Это может занять некоторое время")

        # Показываем статус "печатает"
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing"
        )

        ingredients = [ingredient.strip() for ingredient in user_input.split(',') if ingredient.strip()]

        if not ingredients:
            await status_msg.edit_text("❌ Пожалуйста, укажите хотя бы один ингредиент.")
            return GET_RECIPES

        # Обновляем статус
        await status_msg.edit_text("🌍 Перевожу ингредиенты...")

        # Перевод ингредиентов
        try:
            translated_ingredients = []
            for ingredient in ingredients:
                try:
                    translated = GoogleTranslator(source='ru', target='en').translate(ingredient)
                    translated_ingredients.append(translated)
                except Exception as e:
                    logger.warning(f"Error translating ingredient {ingredient}: {e}")
                    translated_ingredients.append(ingredient)
        except Exception as e:
            logger.error(f"Translation error: {e}")
            await status_msg.edit_text("❌ Ошибка перевода ингредиентов. Попробуйте снова.")
            return GET_RECIPES

        # Обновляем статус
        await status_msg.edit_text("🍳 Ищу рецепты по вашим ингредиентам...")

        # Поиск рецептов
        url = (
            f"https://api.spoonacular.com/recipes/findByIngredients?"
            f"ingredients={','.join(translated_ingredients)}"
            f"&apiKey={SPOONACULAR_API_KEY}"
            f"&number=3"
        )

        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                recipes = response.json()
            except httpx.HTTPStatusError as e:
                logger.error(f"Spoonacular API error: {e}")
                await status_msg.edit_text("❌ Ошибка при получении рецептов. Попробуйте позже.")
                return ConversationHandler.END
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                await status_msg.edit_text("❌ Произошла непредвиденная ошибка.")
                return ConversationHandler.END

        if not recipes:
            await status_msg.edit_text("😞 Не найдено рецептов с указанными ингредиентами.")
            return ConversationHandler.END

        # Удаляем статусное сообщение перед отправкой результатов
        await status_msg.delete()

        # Отправка рецептов
        sent_recipes = 0
        for recipe in recipes:
            try:
                if sent_recipes >= 3:
                    break

                title_en = recipe['title']
                recipe_id = recipe['id']
                image_url = recipe.get('image', '')

                # Обновляем статус для каждого рецепта
                processing_msg = await update.message.reply_text(f"🍽 Обрабатываю рецепт: {title_en}...")

                try:
                    title_ru = GoogleTranslator(source='en', target='ru').translate(title_en)
                except Exception:
                    title_ru = title_en

                recipe_url = f"https://spoonacular.com/recipes/{title_en.replace(' ', '-')}-{recipe_id}"
                translated_url = f"https://translate.google.com/translate?hl=ru&sl=en&u={recipe_url}"

                await processing_msg.delete()  # Удаляем сообщение об обработке

                if image_url.startswith('http'):
                    await update.message.reply_photo(
                        photo=image_url,
                        caption=f"🍽 *{title_ru}*\n\n🔗 [Открыть рецепт]({translated_url})",
                        parse_mode="Markdown"
                    )
                else:
                    await update.message.reply_text(
                        f"🍽 *{title_ru}*\n\n🔗 [Открыть рецепт]({translated_url})",
                        parse_mode="Markdown"
                    )

                sent_recipes += 1
                if sent_recipes < len(recipes[:3]):
                    await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Error processing recipe: {e}")
                continue

    except Exception as e:
        logger.error(f"Unexpected error in get_recipes_handler: {e}")
        await update.message.reply_text("❌ Произошла непредвиденная ошибка при обработке запроса.")

    await show_main_menu(update.message)
    return ConversationHandler.END


async def ask_question_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Обработка вопросов к нейросети с улучшенной обработкой ошибок."""
    try:
        question = update.message.text
        if not question.strip():
            await update.message.reply_text("❌ Пожалуйста, задайте вопрос.")
            return ASK_QUESTION

        # Статусное сообщение
        status_msg = await update.message.reply_text("🧠 Думаю над ответом... Пожалуйста, подождите")

        # Показываем статус "печатает"
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing"
        )

        # Запрос к YandexGPT с таймаутом
        try:
            response = gpt.create_completion(question, 1)
            await status_msg.delete()  # Удаляем статусное сообщение
            await update.message.reply_text(f"🤖 *Ответ:*\n\n{response}", parse_mode="Markdown")
        except Exception as e:
            logger.error(f"YandexGPT error: {e}")
            await status_msg.edit_text("❌ Ошибка при получении ответа от нейросети.")

    except Exception as e:
        logger.error(f"Unexpected error in ask_question_handler: {e}")
        await update.message.reply_text("❌ Произошла непредвиденная ошибка.")

    await show_main_menu(update.message)
    return ConversationHandler.END


async def show_main_menu(message) -> None:
    """Показ главного меню с обработкой ошибок."""
    try:
        keyboard = [
            [
                InlineKeyboardButton("🍳 Получить рецепты", callback_data='get_recipes'),
                InlineKeyboardButton("🧠 Нейросеть", callback_data='ask_question')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await message.reply_text("Выберите действие:", reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in show_main_menu: {e}")


async def handle_regular_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка обычных сообщений, когда нет активного диалога."""
    keyboard = [
        [
            InlineKeyboardButton("🍳 Получить рецепты", callback_data='get_recipes'),
            InlineKeyboardButton("🧠 Нейросеть", callback_data='ask_question')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 Пожалуйста, выберите действие из меню:",
        reply_markup=reply_markup
    )


def main() -> None:
    """Запуск бота с улучшенной обработкой ошибок."""
    try:
        # Настройка Application с параметрами для стабильной работы
        application = Application.builder().token(BOT_TOKEN).build()

        # Настройка ConversationHandler
        conv_handler = ConversationHandler(
            entry_points=[
                CommandHandler("start", start),
                CallbackQueryHandler(button_handler)
            ],
            states={
                GET_RECIPES: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, get_recipes_handler)
                ],
                ASK_QUESTION: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, ask_question_handler)
                ],
            },
            fallbacks=[
                CommandHandler("cancel", cancel),
                CommandHandler("start", start),
                CommandHandler("help", help_command)
            ],
            conversation_timeout=300  # 5 минут таймаут на разговор
        )

        # Добавление обработчиков
        application.add_handler(conv_handler)
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("admin", admin_info))

        # Обработчик для обычных сообщений (добавьте эту строку)
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_regular_message))

        # Запуск бота с настройками
        application.run_polling(
            poll_interval=1.0,
            timeout=20,
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES
        )
    except Exception as e:
        logger.critical(f"Bot crashed: {e}")
        raise


if __name__ == '__main__':
    main()
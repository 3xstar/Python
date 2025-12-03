from tkinter import *
from tkinter import ttk, messagebox
import requests
import json
import base64
from PIL import Image, ImageTk
import io
import os
from dotenv import load_dotenv

load_dotenv()
class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image generator")
        self.root.geometry("950x900")
        self.root.resizable(False, False)

        # API credentials
        self.api_key = os.getenv("API_KEY")
        self.secret_key = os.getenv("SECRET_KEY")
        self.api_url = "https://api-key.fusionbrain.ai/"

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        Label(text="🖼Image generator🖼\nby Zahar Solovyov", font=("Arial", 20, "bold"), foreground="darkblue").pack(pady=10)
        # Main frame
        main_frame = Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Prompt input
        Label(main_frame, text="Описание изображения📑:", font=("Arial", 15, "bold", ), foreground="blue").pack(anchor=CENTER)
        self.prompt_entry = Text(main_frame, height=5, width=80, font=("Arial", 10))
        self.prompt_entry.pack(pady=(0, 20))

        # Style selection
        Label(main_frame, text="Стиль изображения👔:", font=("Arial", 15, "bold"), foreground="blue").pack(anchor=W)
        self.style_var = StringVar(value="ANIME")
        styles = ["ANIME", "DEFAULT", "UHD", "CLASSIC", "3D", "FLAT"]
        self.style_menu = ttk.Combobox(main_frame, textvariable=self.style_var, background="ghostwhite", values=styles, state="readonly")
        self.style_menu.pack(fill=X, pady=(0, 20))

        # Size selection
        size_frame = Frame(main_frame)
        size_frame.pack(fill=X, pady=(0, 20))

        Label(size_frame, text="Размер изображения📏:", font=("Arial", 15, "bold"), foreground="blue").pack(anchor=W)

        self.size_var = StringVar(value="1024x1024")
        sizes = ["512x512", "768x768", "1024x1024", "1024x768", "768x1024"]
        for size in sizes:
            Radiobutton(size_frame, text=size, variable=self.size_var, value=size).pack(side=LEFT, padx=10)

        # Generate button
        self.generate_btn = Button(main_frame, text="🕔Сгенерировать изображение✅",
                                   command=self.generate_image, font=("Arial", 15, "bold"), bg="#4CAF50", fg="white")
        self.generate_btn.pack(pady=5)

        # Image display
        self.image_label = Label(main_frame)
        self.image_label.pack(fill=BOTH, expand=True)

        # Status bar
        self.status_var = StringVar(value="Готов к работе")
        Label(main_frame, textvariable=self.status_var, bd=1, relief=SUNKEN, anchor=W).pack(fill=X)

    def generate_image(self):
        prompt = self.prompt_entry.get("1.0", END).strip()
        if not prompt:
            messagebox.showwarning("Ошибка", "Введите описание изображения")
            return

        style = self.style_var.get()
        width, height = map(int, self.size_var.get().split('x'))

        self.status_var.set("Генерация изображения...")
        self.root.update()

        try:
            # Initialize API
            auth_headers = {
                'X-Key': f'Key {self.api_key}',
                'X-Secret': f'Secret {self.secret_key}',
            }

            # Get pipeline
            response = requests.get(self.api_url + 'key/api/v1/pipelines', headers=auth_headers)
            pipeline_id = response.json()[0]['id']

            # Generate image
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
                'pipeline_id': (None, pipeline_id),
                'params': (None, json.dumps(params), 'application/json')
            }

            response = requests.post(self.api_url + 'key/api/v1/pipeline/run',
                                     headers=auth_headers, files=data)
            request_id = response.json()['uuid']

            # Check generation status
            self.status_var.set("Ожидание завершения генерации...")
            self.root.update()

            result = None
            for _ in range(10):  # 10 attempts with 10 sec delay
                response = requests.get(self.api_url + 'key/api/v1/pipeline/status/' + request_id,
                                        headers=auth_headers)
                data = response.json()

                if data['status'] == 'DONE':
                    image_data = base64.b64decode(data['result']['files'][0])
                    self.display_image(image_data)
                    self.status_var.set("Генерация завершена!")
                    return

                self.root.after(10000)  # 10 sec delay
                self.root.update()

            messagebox.showerror("Ошибка", "Превышено время ожидания генерации")
            self.status_var.set("Ошибка генерации")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
            self.status_var.set("Ошибка")

    def display_image(self, image_data):
        image = Image.open(io.BytesIO(image_data))

        # Resize for display while maintaining aspect ratio
        max_size = (600, 400)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)

        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference


if __name__ == '__main__':
    root = Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
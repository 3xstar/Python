from datetime import datetime
current_date = datetime.now().strftime('%d.%m.%Y')

with open('log.txt', 'a') as file:
    error_text = input("Введите сообщение об ошибке: ")
    file.write(f"ERROR [{current_date}]: {error_text}\n")
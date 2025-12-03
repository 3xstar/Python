try:
    with open('file.txt', 'x', encoding='UTF-8') as file:
        file.write('ТЕКСТ')
except FileExistsError:
    print("Данный файл уже существует")
# Через контекстный мессенджер with as
with open('file2.txt', 'w', encoding='UTF-8') as file:
    file.write('Очень важное сообщение')

with open('file2.txt', 'r', encoding='UTF-8') as file:
    print(file.read())

    
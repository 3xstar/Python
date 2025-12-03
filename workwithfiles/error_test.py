with open('file3.txt', 'a', encoding='UTF-8') as file:
    file.write('\nСообщение')

with open('file3.txt', 'x', encoding='UTF-8') as file:
    file.write('ТЕКСТ')
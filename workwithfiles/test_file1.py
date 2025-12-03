# Пример записи
file = open('file1.txt', 'w', encoding='UTF-8')
file.write('Новое сообщение')
file.close()

# Пример чтения
file = open('file1.txt', 'r', encoding='UTF-8')
print(file.read())
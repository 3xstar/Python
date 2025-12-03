with open('file2.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())
    print('\n')
    print(file.read())
    print(file.tell()) # Вывод текущей позиции курсора
    print(file.seek(0)) # Возврат курсора к началу
    print(file.read())
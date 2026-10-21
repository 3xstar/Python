# Способы чтения

# read() - вывод всего
with open('file2.txt', 'r', encoding='UTF-8') as file:
    print(file.read())

# readline() - вывод одной строчки
with open('file2.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())

# readlines() - вывод всех строк файла списком
with open('file2.txt', 'r', encoding='UTF-8') as file:
    print(file.readlines())

# with open('file2.txt', 'r', encoding='UTF-8') as file:
#    print(file.read())
#    print(file.readlines()) - НЕЛЬЗЯ, ТАК КАК КУРСОР ПОСЛЕ READ НАХОДИТСЯ В КОНЦЕ
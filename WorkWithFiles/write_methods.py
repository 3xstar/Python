# write - вписать строки в файл
with open('file2.txt', 'w', encoding='UTF-8') as file:
    file.write('Очень важное сообщение')

# writelines - вписать в файл список строк
with open('file2.txt', 'w', encoding='UTF-8') as file:
    file.writelines(['Очень важное сообщение', 'Не важное сообщение'])

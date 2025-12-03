# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации
human_info = {1: "ФИО = Соловьёв Захар Олегович", 2: "Телефон = +79246274877", 3: "email = tmrniket@gmail.com",
        4: "Название должности = программист", 5: "Номер кабинета = 200", 6: "telegram = @bruhlmaocringe"}
print("Информация:", human_info)
while True:
    try:
        def action_menu():
            print("\n1. Добавить данные"
                  "\n2. Удалить данные"
                  "\n3. Поиск данных"
                  "\n4. Замена данных")
            action = int(input("\nВведите номер действия: "))
            match action:
                case 1:
                    new_info = []
                    definition = input("Введите определение новых данных: ")
                    new_info.append(definition)
                    example = input("Введите новые данные: ")
                    new_info.append(example)
                    info_list = list(human_info)
                    human_info[len(info_list) + 1] = f"{new_info[0]} = {new_info[1]}"
                    print(f"\nНовые данные: {human_info[len(info_list) + 1]}, добавлены")
                    print("Информация: ", human_info)


                case 2:
                    index = int(input("\nВведите номер данных для удаления: "))
                    for key, value in list(human_info.items()):
                        if index == key:
                            del human_info[key]
                    print("\nДанные удалены")
                    print("Информация: ", human_info)

                case 3:
                    int_index = int(input("\nВведите порядковый номер данных: "))
                    for key, value in human_info.items():
                        if int_index == key:
                            print("\nДанные под этим номером: ", value)

                case 4:
                    int_index = int(input("\nВведите номер слова для замены данных: "))
                    for key, value in list(human_info.items()):
                        if int_index == key:
                            new_info = []
                            definition = input("Введите определение новых данных: ")
                            new_info.append(definition)
                            example = input("Введите новые данные: ")
                            new_info.append(example)
                            info_list = list(human_info)
                            human_info[key] = f"{new_info[0]} = {new_info[1]}"
                            print(f"\nОбновленные данные: {human_info[key]}")
                            print("Информация: ", human_info)
        action_menu()
    except Exception:
        print("В программе произошла ошибка, попробуйте снова")
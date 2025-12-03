# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.
basketball_players = {1: ["Соловьёв Захар Олегович", 190],
                              2: ["Ломанов Вадим Радионович", 150],
                              3: ["Сюзюмов Максим Максимович", 170]
                              }
print("Список игроков:", basketball_players)
while True:
    try:
        def action_menu():
            print("\n1. Добавить игрока"
                  "\n2. Удалить игрока"
                  "\n3. Поиск игрока"
                  "\n4. Замена данных игрока")
            action = int(input("\nВведите номер действия: "))
            match action:
                case 1:
                    new_player = []
                    name = input("\nВведите ФИО нового игрока: ")
                    new_player.append(name)
                    height = int(input("Введите рост нового игрока: "))
                    new_player.append(height)
                    list_bp = list(basketball_players)
                    basketball_players[len(list_bp) + 1] = new_player
                    print(f"Игрок: {new_player} добавлен")
                    print("Список игроков:", basketball_players)

                case 2:
                    index = int(input("\nВведите номер игрока для удаления: "))
                    for key, value in list(basketball_players.items()):
                        if index == key:
                            del basketball_players[key]
                    print("\nИгрок удален")
                    print("Список игроков:", basketball_players)

                case 3:
                    int_index = int(input("\nВведите рост или порядковый номер игрока: "))
                    for key, value in basketball_players.items():
                        if int_index == value[1] or int_index == key:
                            print("\nФИО данного игрока: ", value[0])
                            print("Список игроков:", basketball_players)

                case 4:
                    int_index = int(input("\nВведите номер игрока для замены данных: "))
                    for key, value in list(basketball_players.items()):
                        if int_index == key:
                            basketball_players[key].clear()
                            new_player = []
                            name = input("Введите ФИО нового игрока: ")
                            new_player.append(name)
                            height = int(input("Введите рост нового игрока: "))
                            new_player.append(height)
                            basketball_players[key] = new_player
                            print("\nИгрок с обновленными данными: ",basketball_players[key])
                            print("Список игроков:", basketball_players)
        while True:
            action_menu()
    except Exception:
        print("В программе произошла ошибка, попробуйте снова")

class Character:
    def __init__(self, name, hp, damage, ability, direction):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.ability = ability
        self.direction = direction

    def char_info(self):
        print(f"Название класса: {self.name}")
        print(f"Количество здоровья: {self.hp}")
        print(f"Наносимый урон за атаку: {self.damage}")
        print(f"Способность класса: {self.ability}")
        print(f"Направление класса: {self.direction}")

zombie = Character("Zombie", 200, 40, "Укус врага с последующим кровотечением",
                   "Медленный танк, наносящий огромный урон в ближнем бою")

alchemist = Character("Alchemist", 125, 15,
                      "Атака случайной стихией, накладывающая соответствующий ей эффект",
                   "Дальник с малым уроном, но хорошей мобильностью и полезной способностью")

witch = Character("Witch", 75, 30,
                  "Может восстанавливать здоровье в бою путем выпивания зелий",
                   "Класс, способный атаковать на ближней и дальней дистанции с неплохим уроном,"
                   "но малым количеством здоровья")

characters = [zombie, alchemist, witch]

enemy = [zombie, alchemist, witch]

tavern = []

player = []

choice_class = int(input("1 - Зомби\n"
              "2 - Алхимик\n"
              "3 - Ведьма\n"
              "Выберите класс: "))

match choice_class:

    case 1:
        player.append(zombie)
        print("Выбран класс: Зомби")

    case 2:
        player.append(alchemist)
        print("Выбран класс: Алхимик")

    case 3:
        player.append(witch)
        print("Выбран класс: Ведьма")

choice_action = int(input("1 - Отобразить информацию о своем классе\n"
                          "2 - Сразиться с персонажем другого класса\n"
                          "3 - Отправить персонажа в таверну (приводит к выбору другого класса)\n"
                          "Выберите действие: "))

match choice_action:

    case 1:
        for i in player:
            i.char_info()

    case 2:
        for i in enemy:
            print(enemy.index(i), i.name)
        choice_enemy = int(input("Выбери своего оппонента (0 - 3): "))
        player_enemy_hp = [player[0].hp, enemy[choice_enemy].hp]
        while player_enemy_hp[0] != 0 or player_enemy_hp[1] != 0:
            print(f"Ваше количество здоровья: {player_enemy_hp[0]}")
            print(f"Колиество здоровья врага: {player_enemy_hp[1]}")
            fight_action = int(input("1 - Атаковать врага\n"
                                    "2 - Поставить блок\n"
                                    f"3 - Использовать свою способность: {player[0].ability}\n"
                                    "Выберите действие: "))
            player_enemy_hp[1] -= player[0].damage
            print("Вы нанесли удар!")
            print(f"Вы опустили здоровье врага до: {player_enemy_hp[1]}")
        else:
            print("Игра окончена")

    case 3:
        for i in player:
            tavern.append(i)
        print("Персонаж отправлен в таверну")
        print("Находящиеся в таверне:")
        for i in tavern:
            print(i.name)

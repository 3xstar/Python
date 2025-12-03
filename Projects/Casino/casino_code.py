def game():
    import random
    balance = 1000
    rand_bet = random.randint(1, 10)
    print("Приветствуем в тебя в 1XRAZVODILOVO")
    while True:
        choice = input("Начать игру? (да или нет): ")
        # if choice.lower() == 'да'
        if choice in 'ДадаДА':
            print("Ставка 0 = конец игры")
            while True:
                print("Ваш баланс: ", balance)
                bet = int(input("Введите ставку: "))
                if balance >= bet >= 1:
                    bet_number = int(input("Введите число в диапозоне от 1 до 10: "))
                    if balance >= bet >= 1:
                        if 10 >= bet_number >= 1:
                            if bet_number == rand_bet:
                                balance += bet
                                print("Вы выиграли")
                            else:
                                balance -= bet
                                print("Вы проиграли")
                        else:
                            print("Вы ввели число не в диапозоне 10, попробуйте снова")
                elif bet == 0:
                    print("Игра окончена, ваш баланс: ", balance)
                    break
                else:
                    print("Вы ввели ставку не в пределах вашего баланса, попробуйте снова")
        elif choice == "нет" or choice == "Нет" or choice == "НЕТ":
            print("Передумай")
        else:
            print("Введи нормальный ответ")
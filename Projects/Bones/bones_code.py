def game():
    print("Игра 'Кости'")
    while True:
        try:
            import random
            balance = 1000
            print("Ваш баланс:", balance)
            balance_bet = int(input("Введите сумму, которую хотите поставить: "))
            bet = input("Введите ставку (пас или не пас): ")

            def drop_cube():
                print("\nВы бросаете кубик 2 раза")
                drop1 = (random.randint(1, 6))
                print("Первый бросок: ", drop1)
                drop2 = (random.randint(1, 6))
                print("Второй бросок: ", drop2)
                points = drop1 + drop2
                print("Сумма очков на кубике: ", points)
                return points

            def bet_check(points):
                new_balance = balance - balance_bet
                if points == 7 or points == 11:
                    if bet in "Пас пас ПАС":
                        print("\nВы выиграли ставку")
                        new_balance += balance_bet * 2

                    elif bet in "Не пас""НЕ ПАС""не пас":
                        print("\nВы проиграли ставку")

                if points == 2 or points == 3 or points == 12:
                    if bet in "ПаспасПАС":
                        print("\nВы проиграли ставку")

                    elif bet in "Не пас""НЕ ПАС""не пас":
                        print("\nВы выиграли ставку")
                        new_balance += balance_bet * 2

                if points == 4 or points == 5 or points == 6 or points == 8 or points == 9 or points == 10:
                    period = points
                    new_points = 0
                    while new_points != period or new_points != 7:
                        print("Выпало значение, которое становится периодом")
                        print("Перебрасывание")
                        new_points = drop_cube()

                        if new_points == period:
                            if bet in "ПаспасПАС":
                                print("\nВы выиграли ставку")
                                new_balance += balance_bet * 2
                                break

                            elif bet in "Не пас""НЕ ПАС""не пас":
                                print("\nВы проиграли ставку")

                        elif new_points == 7:
                            if bet in "ПаспасПАС":
                                print("\nВы проиграли ставку")
                                break

                            elif bet in "Не пас""НЕ ПАС""не пас":
                                print("\nВы выиграли ставку")
                                new_balance += balance_bet * 2
                                break

                    print("Ваш баланс: ", new_balance)
                    return new_balance

            balance = bet_check(drop_cube())

            while True:
                choice = input("\nПродолжить игру? (да или нет): ")
                if choice in "ДадаДА":
                    balance_bet = int(input("\nВведите сумму, которую хотите поставить: "))
                    bet = input("\nВведите ставку (пас или не пас): ")
                    balance = bet_check(drop_cube())
                if choice in "НетнетНЕТ":
                    print("Игра окончена")
                    break
        except Exception:
            print("В программе произошла ошибка, попробуйте снова")
game()
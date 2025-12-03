def game():
    import random
    random_number = random.randint(1,1000)
    print("Игра - угадай число!")
    print("Вы должны угадать случайное число в диапозоне от 1 до 1000 по подсказкам:\n'больше' или 'меньше'")
    while True:
        first_number = int(input("\nВведите предполагаемое число: "))
        if first_number != random_number:
            if first_number > random_number:
                print("\nВаше число больше")
            if first_number < random_number:
                print("\nВаше число меньше")
            while first_number != random_number:
                first_number = int(input("\nВведите предполагаемое число: "))
                if first_number > random_number:
                    print("\nВаше число больше")
                if first_number < random_number:
                    print("\nВаше число меньше")
            else:
                while True:
                    action = input("\nВы угадали загаданное число, продолжить игру? (да или нет): ")
                    if action in "ДадаДА":
                        random_number = random.randint(1, 100000)
                        first_number = int(input("\nВведите предполагаемое число: "))
                        if first_number != random_number:
                            if first_number > random_number:
                                print("\nВаше число больше")
                            if first_number < random_number:
                                print("\nВаше число меньше")
                            while first_number != random_number:
                                first_number = int(input("\nВведите предполагаемое число: "))
                                if first_number > random_number:
                                    print("\nВаше число больше")
                                if first_number < random_number:
                                    print("\nВаше число меньше")
                    if action in "НетнетНЕТ":
                        print("Игра окончена")
                        break
                    else:
                        print("Введите значение 'да' или 'нет'")


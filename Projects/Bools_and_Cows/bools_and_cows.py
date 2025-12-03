# ». Программа «загадывает» четырёхзначное число и играющий должен угадать его.
# После ввода пользователем числа программа сообщает, сколько цифр числа угадано (быки)
# и сколько цифр угадано и стоит на нужном месте (коровы). После отгадывания числа на
# экран необходимо вывести количество сделанных пользователем попыток.
# В программе необходимо использовать рекурсию.
import random
from operator import index
def game():
    random_number = (random.randint(1000,9999))
    tries = 0
    while True:
        player_number = int(input("\nПопробуйте угадать четырехзначное число: "))
        bools = 0
        cows = 0
        if len(str(player_number)) == 4:
            if player_number != random_number:
                tries += 1
                for i in str(player_number):
                    for c in str(random_number):
                        if i == c:
                            bools += 1
                        if i == c and str(player_number).index(i) == str(random_number).index(c):
                            cows += 1
                print("Было обнаружено быков: ", bools)
                print("Было обнаружено коров: ", cows)
            elif str(player_number) == str(random_number):
                print("Вы угадали загаданное число!")
                print("Количество потраченных попыток: ", tries)
                action = input("Продолжить игру? (да или нет): ")
                if action in "ДадаДА":
                    game()
                else:
                    print("Игра окончена")
                    break
        elif len(str(player_number)) != 4:
            print("Вы ввели не четырехзначное число, попробуйте снова")






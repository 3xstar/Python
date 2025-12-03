diametr = int(input("Введите диаметр окружности: "))
option = input("Выберите операцию (S - площадь, P - периметр): ")
P = 3.1415
if option == "S":
    print(2 * P * diametr)
elif option == "P":
    print(P * (diametr**2))
else:
    print("Вы ввели неверные данные")

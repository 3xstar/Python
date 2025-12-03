def figures():
    import math
    while True:
        try:
            figure = int(input("1 - круг\n"
                               "2 - квадрат\n"
                               "3 - прямоугольник\n"
                               "Выберите фигуру для вычислений: "))
            match figure:
                case 1:
                    radius = int(input("Введите радиус круга (окружности): "))
                    P = (2 * math.pi) * radius
                    S = math.pi * (radius**2)
                    print(f"Периметр круга равен: {P}\n"
                          f"Площадь круга равна: {S}")
                case 2:
                    side = int(input("Введите значение стороны квадрата: "))
                    P = 4 * side
                    S = side ** 2
                    print(f"Периметр квадрата равен: {P}\n"
                          f"Площадь квадрата равна: {S}")
                case 3:
                    side1 = int(input("Введите значение 1 стороны прямоугольника: "))
                    side2 = int(input("Введите значение 2 стороны прямоугольника: "))
                    P = 2 * (side2 + side2)
                    S = side1 * side2
                    print(f"Периметр прямоугольника равен: {P}\n"
                          f"Площадь прямоугольника равна: {S}")
        except Exception:
            print("В программе произошла ошибка, попробуйте снова")
figures()



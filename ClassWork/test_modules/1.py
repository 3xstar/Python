def triangle():
    while True:
        try:
            corner1 = int(input("Введите количество градусов 1 угла: "))
            corner2 = int(input("Введите количество градусов 2 угла: "))
            corner3 = int(input("Введите количество градусов 3 угла: "))
            if corner1 + corner2 + corner3 != 180:
                print("Сумма градусов либо больше, либо меньше 180, попробуйте снова")
            else:
                print(f"A = {corner1}")
                print(f"B = {corner2}")
                print(f"C = {corner3}")
                if corner1 == 90 or corner2 == 90 or corner3 == 90:
                    print("Треугольник является прямоугольным")
                elif corner1 > 90 or corner2 > 90 or corner3 > 90:
                    print("Треугольник является тупоугольным")
                elif corner1 < 90 and corner2 < 90 and corner3 < 90:
                    print("Треугольник является остроугольным")
                    if corner1 == 60 and corner2 == 60 and corner3 == 60:
                        print("И также равносторонним")
        except Exception:
            print("В программе произошла ошибка, попробуйте снова")
triangle()
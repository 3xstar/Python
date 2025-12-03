def square():
    while True:
        try:
            line = int(input("Введите длину линии: "))
            symbol = input("Введите желаемый символ: ")
            print("True = заполненный квадрат, False = пустой квадрат")
            status = input("Введите желаемый вид квадрата (True или False): ")
            squareline = line * symbol
            if status == "True":
                for i in range(line):
                    print(squareline)
            elif status == "False":
                print(squareline)
                for i in range(line):
                    print(symbol + " " * (line - 2) + symbol)
                print(squareline)
            else:
                print("В программе была допущена ошибка")
        except Exception:
            print("В программе была допущена ошибка")
square()
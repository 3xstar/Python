def input_int(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Вы ввели не число, попробуйте снова: ")


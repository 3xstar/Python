def check_int(help="Введите число: "):
    while True:
        try:
            a = input(help)
            a = int(a)
            return (a)
        except ValueError:
            print("Вы ввели не число, попробуйте снова")
a = check_int()
def func_count(a):
    a = str(a)
    print("Количество цифр в данном числе: ")
    print(len(a))
func_count(a)
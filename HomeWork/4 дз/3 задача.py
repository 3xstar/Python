number = int(input("Введите номер месяца (1-12): "))
if number == 1 or number == 2 or number == 12:
    print("Winter")
elif number == 3 or number == 4 or number == 5:
    print("Spring")
elif number == 6 or number == 7 or number == 8:
    print("Summer")
elif number == 9 or number == 10 or number == 11:
    print("Autumn")
else:
    print("Вы ввели число не в диапазоне 1-12")
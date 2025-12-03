number = input("Введите 6-значное число: ")
if len(number) == 6:
    sum1 = int(number[0]) + int(number[1]) + int(number[2])
    sum2 = int(number[3]) + int(number[4]) + int(number[5])
    if sum1 == sum2:
        print("Число является счастливым")
    else:
        print("Число является не счастливым")
else:
    print("Число не 6-ти значное")

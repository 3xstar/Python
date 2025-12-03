sec = int(input("Введите количество секунд: "))
sec_in_day = 24 * 60 * 60
option = input("Выберите часы, минуты или секунды: ")
if option == "часы":
    print("До полуночи: ", (sec_in_day - sec) / 60 / 60)
elif option == "минуты":
    print("До полуночи:", (sec_in_day - sec) / 60)
elif option == "секунды":
    print("До полуночи:", (sec_in_day - sec))
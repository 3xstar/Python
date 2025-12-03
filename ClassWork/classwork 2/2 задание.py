dollar = 100
euro = 110
while True:
    money = int(input("Введите количество валюты: "))
    while True:
        user_valute = input("Введите название валюты: ")
        if user_valute == "рубль":
            user_rub = money
            user_dollar = money / dollar
            user_euro = money / euro
        elif user_valute == "доллар":
            user_dollar = money
            user_rub = money * dollar
            user_euro = user_rub / euro
        elif user_valute == "евро":
            user_euro = money
            user_rub = money * euro
            user_dollar = user_rub / dollar
        else:
            print("Нет такой валюты")
            continue
        break
    while True:
        target_valute = input("Введите валюту которая нужна: ")
        if target_valute == "доллар":
            print(money,user_valute, "в долларах: ", user_dollar)
        elif target_valute == "евро":
                print(money, user_valute, "в евро: ", user_euro)
        elif target_valute == "рубль":
                print(money, user_valute, "в рублях: ", user_rub)
        else:
            print("Нет такой валюты")
            continue
        break

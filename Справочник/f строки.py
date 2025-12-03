name = "Zahar"
age = 16.234
# string = "{} сколько тебе лет?".format(name)
string = f"{name} сколько тебе лет? "
print(string)
answer = input(f"{name}, тебе {age:6.2f} лет поэтому, введи номер твоей карты: ")
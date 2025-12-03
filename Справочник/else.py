print("hello","world")
print("hello","world",end = "\n lol \n")
print("hello","world")

print("я","уже","настолько","преисполнился", sep = "\n")

print("что мне этот \t \"world\" уже понятен")

a = 5
b = 6
print(a != b)

#and - и
#or - или
#not - не

print(a != b and a >= 5)
print(a == b or b != a)
print(not (a < b) or not(b != a))

# True False - булевые значения, это тип данных bool

print(bool(0))

a = 3
if a > 1:
    print("hello 3")

age = int(input("насколько ты стар?"))
if age < 18:
    print("У тебя еще вся жизнь впереди сосунок")
elif age >= 30:
    print("Олды на месте")
else:
    print("Чао персик, дозревай")

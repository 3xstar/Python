a = [] #пустой список
lol = [1, 2, 3, 4, 5, "1", "a", "ololol", a]
c = list() #пустой список
c1 = list((1, 2, 3, 4)) #не пустой список
c2 = list("maxim")
print(c2)

students = ["Дима", "Марк", "Влад"]
print(students)
print(students[0])
print(students[0:3])

# for i in range(3):
#     print(students[i], end="  ")
while True:
    action = input("что надо? ")
    if action == "добавить":
        stud = input("Введите имя: ")
        students.append(stud)
    if action == "добавить в топ":
        stud = input("Введите имя: ")
        students.insert(0, stud)
    if action == "удалить":
        stud = input("Введите имя: ")
        students.remove(stud)
    if action == "удалить по номеру":
        stud = input("Введите номер: ")
        a = students.pop(int(stud)-1)
        print("Был удален: ", a)
    if action == "индекс":
        stud = input("Введите имя: ")
        a = students.index(stud)
        print(stud, "Находится на месте: ", a + 1)
    if action == "отсортировать":
        students.sort()
    if action == "отчислить всех":
        students.clear()

    for i in students:
        print(i)
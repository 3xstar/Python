anecdot = {1: "анекдот 1", 2: "анекдот 2"}

print(anecdot[1])

print(anecdot.keys()) #вернуть ключи
print(anecdot.values()) #вернуть значения
print(anecdot.items()) #вернуть пары ключ значения

anecdot[1] = "Колобок повесился"
print(anecdot[1])

anecdot.pop(1) #удалить по ключу
print(anecdot)

new_item = dict([(3, "анекдот 3")])
new_item.update([(3, "анекдот 3"), (4, "анекдот 4")]) #добавить по ключу
anecdot.update(new_item)
print(anecdot)

del anecdot[4] #удалить по ключу
print(anecdot)

anecdot[5] = "анекдот 5" #добавить по ключу
print(anecdot)

print("Ключи: ")
for key in anecdot.keys():
    print(key, end =" ")

print("\nЗначения: ")
for value in anecdot.values():
    print(value, end =" ")

print("\nПары: ")
for key, value in anecdot.items():
    print(key, "-", value)


for key, value, item in zip(anecdot.keys(),anecdot.values(), anecdot.items()):
    print(key, value, item, sep=" - ")
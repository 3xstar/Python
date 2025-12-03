# join соединение списка в строку

numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     numbers[i] = str(numbers[i])
numbers = map(str,numbers)
string = "".join(numbers)
print(string)

#split разъеденение строки в список
ip = "192.168.88.16"
ip = ip.split(".")
print(ip)

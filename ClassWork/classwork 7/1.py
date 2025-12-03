def input_int_list():
    while True:
        try:
            numbers = input("Введите числа через пробел: ")
            numbers_list = numbers.split()
            for i in range(len(numbers_list)):
                numbers_list[i] = int(numbers_list[i])
            return numbers_list
        except ValueError:
            ("Вы ввели не число, попробуйте снова")
def pow_list(list, x):
    for i in range(len(list)):
        list[i] = list[i] ** x
    return list
# numbers = input_int_list()
# numbers = pow_list(numbers, 5)
numbers = pow_list(input_int_list(), 5)
print(numbers)

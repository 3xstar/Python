def print_data():
    with open("data.txt", "r+", encoding="utf-8") as file:
        data = file.read()

    print("Содержимое файла: ")
    print(data)

# print_data()

def sum_items():
    with open("data.txt", "r+", encoding="utf-8") as file:
        data = file.read()

    data = data.split()
    first_item = 0
    second_item = 2

    with open("corrected_data.txt", "w+", encoding="utf-8") as corrected_file:

        def recursion(first_element, second_element):
            try:
                if data[first_element] != data[second_element]:
                    while data[first_element] != data[second_element]:
                        second_element += 1
                    else:
                        number = int(data[first_element + 1]) + int(data[second_element + 1])
                        print(data[first_element], number)
                        corrected_file.write(f"{data[first_element]} {number} \n")
                        first_element += 2
                        second_element = first_element + 2
                        recursion(first_element, second_element)
            except IndexError:
                print("Данные записаны в исправленный файл")

        recursion(first_item, second_item)

sum_items()

def statistic():
    with open("corrected_data.txt", "r+", encoding="utf-8") as file:
        data = file.read()

    data = data.split()
    summ = 0
    index = 1

    def recursion(i, j):
        try:
            i += int(data[j])
            j += 2
            recursion(i, j)
        except IndexError:
            print("Общее количество товаров:", i)
    recursion(summ, index)

    list_of_numbs = [int(data[1]), int(data[3]), int(data[5])]
    max_count = max(list_of_numbs)

    j = 0
    while data[j] != str(max_count):
        j += 1
    else:
        print("Самый популярный товар:", data[j - 1])

statistic()
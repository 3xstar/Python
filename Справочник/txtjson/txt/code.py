# my_life = ["родился", "пошел в школу", "пошел в техникум", "поработал", "состарился", "умер"]
#
# file = open("mylife.txt", "w+", encoding = "utf-8")
#
# file.write("История моей жизни \n")
#
# for i in range(len(my_life)):
#     my_life[i] = "\t" + my_life[i].capitalize() +"\n"
#
# file.writelines(my_life)
#
# file.close()

# with open("mylife.txt", "a", encoding = "utf-8") as file:
#     content = file.write("Истории конец, а кто слушал - молодец")

with open("mylife.txt", "r+", encoding = "utf-8") as file:
    content = file.readline()
    print(content, end="")
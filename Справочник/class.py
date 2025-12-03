class Student:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_info(self):
        print(f"имя {self.name}")
        print(f"возраст {self.age}")
        print(f"цвет {self.age}")


grisha = Student("Гриша", 80, "black")
zahar = Student("Захар", 90, "black")
grisha.get_info()
zahar.get_info()

from abc import  *

class Transport(ABC):
    @abstractmethod
    def move(self, status):
        pass


    def show_info(self, name, info):
        pass


class Car(Transport):
    def move(self, status):
        status = True
        if status is True:
            print(f"Машина заведена")

    def show_info(self, name, info):
        print(f"Название транспорта: {name}\nИнформация о транспорте: {info}")


class Plane(Transport):
    def move(self, status):
        status = True
        if status is True:
            print(f"Самолет заведен")

    def show_info(self, name, info):
        print(f"Название транспорта: {name}\nИнформация о транспорте: {info}")


class Boat(Transport):
    def move(self, status):
        status = True
        if status is True:
            print(f"Лодка заведена")

    def show_info(self, name, info):
        print(f"Название транспорта: {name}\nИнформация о транспорте: {info}")

matiz = Car()
boeing = Plane()
bismarck = Boat()

matiz.move(status=False)
boeing.move(status=False)
bismarck.move(status=False)

matiz.show_info("Матизик", "Маленький миленький")
boeing.show_info("Боинчик", "Любит влетать в 2 башни")
bismarck.show_info("Бисмарчик", "Любимая лодка канцлера")




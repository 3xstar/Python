class Airplane:
    def fly(self):
        print("Полетели")

class Ship:
    def fly(self):
        print("Корабль полетел")

    def swim(self):
        print("Поплыли")

class Car(Airplane, Ship):
    def drive(self):
        print("Вин дизель")

c = Car()
c.fly()
c.drive()
c.swim()

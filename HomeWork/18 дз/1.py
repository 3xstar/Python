import math

class CircleSquare:
    def __init__(self, radius):
        self.radius = radius

    def input(self):
        self.radius = int(input("Введите радиус окружности: "))

    def square_area(self):
        square_area = 2 * (self.radius ** 2)
        print("\nПлощадь квадрата: ", square_area)
        circle_area = math.pi * (self.radius**2)
        print("Площадь окружности: ", circle_area)

test_radius = CircleSquare(0)
test_radius.input()
test_radius.square_area()


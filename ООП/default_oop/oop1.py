class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @classmethod
    def add(self):
        return self.num1 + self.num2
    
    @staticmethod
    def info():
        print("Данный класс предназначен для работы с математическими вычислениями")

    @staticmethod
    def formuls():
        print("Формула площади квадрата: blabla;\nФормула периметра квадрата: bleble")
    
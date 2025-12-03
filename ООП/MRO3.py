#Миксин - это класс, который расширяет функционал, но не затрагивает структуру
class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, c, b, a):
        super().__init__(14)
        super().__init__(15)
        self.c = c
        self.b = b
        self.a = a

    def do(self):
        print(self.a, self.b, self.c)

c = C(10, 15, 4)
c.do()
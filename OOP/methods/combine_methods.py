# Комбинированный пример: Создание типа данных - Array

class Array:
    def __init__(self, *components):
        self.components = list(components)

    # Реализация суммирования
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError('Длина массивов должна быть одинаковой')
        result = [a + b for a, b in zip(self.components, other.components)]
        return Array(*result)

    # Реализация вычитания
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError('Длина массивов должна быть одинаковой')
        result = [a - b for a, b in zip(self.components, other.components)]
        return Array(*result)

    # Реализация получения длины массива
    def __len__(self):
        return len(self.components)

    # Реализация получения значения по индексу из массива
    def __getitem__(self, index):
        return self.components[index]

    def __repr__(self):
        return f'Array({", ".join(map(str, self.components))})'

v1 = Array(1, 7, 21)
v2 = Array(14, 2, 43)
print(v1 + v2) # Суммирование
print(v2 - v1) # Вычитание
print(len(v1), len(v2)) # Количество элементов
print(v1[1], v2[2]) # Значения по индексу
# Примечание: добавить функции map(), reduce(), filter() в перечень тем для изучения
class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError('Длина векторов должна быть одинаковой')
        result = [a + b for a, b in zip(self.vector, other.vector)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError('Длина векторов должна быть одинаковой')
        result = [a - b for a, b in zip(self.vector, other.vector)]
        return Vector(result)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        return self.vector[index]

    def __repr__(self):
        return f'Vector({", ".join(map(str, self.vector))})'

    def __eq__(self, other):
        if len(self.vector) != len(other.vector):
            return False
        return all(a == b for a, b in zip(self.vector, other.vector))

    def __mul__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError('Длина векторов должна быть одинаковой')
        result = sum(a * b for a, b in zip(self.vector, other.vector))
        return result

    def __abs__(self):
        not_full_result = sum(x * x for x in self.vector)
        result = not_full_result ** 0.5
        return result

    def __iter__(self):
        return iter(self.vector)
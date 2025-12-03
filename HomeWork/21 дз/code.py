import numpy as np


# Функция активации - преобразует вход в диапазон 0-1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Производная сигмоиды - для расчета градиентов
def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, x, y):
        # Инициализация сети:
        # - входные данные (x)
        # - веса (случайные значения)
        # - ожидаемый вывод (y)
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)  # Веса между входом и скрытым слоем
        self.weights2 = np.random.rand(4, 1)  # Веса между скрытым слоем и выходом
        self.y = y
        self.output = np.zeros(y.shape)  # Пока выход нулевой
        self.layer1 = None  # Скрытый слой

    def feedforward(self):
        # Прямой проход:
        # 1. Умножаем вход на веса -> применяем сигмоиду -> получаем скрытый слой
        # 2. Умножаем скрытый слой на веса -> применяем сигмоиду -> получаем выход
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        return np.mean(np.square(self.y - self.output))  # Возвращаем ошибку

    def backprop(self):
        # Обратное распространение ошибки:
        # 1. Считаем ошибку на выходе
        # 2. Вычисляем градиенты (как сильно влияет каждый вес на ошибку)
        # 3. Корректируем веса в сторону уменьшения ошибки

        # Градиенты для выходного слоя
        output_error = self.y - self.output
        output_delta = output_error * sigmoid_derivative(self.output)

        # Градиенты для скрытого слоя
        layer1_error = output_delta.dot(self.weights2.T)
        layer1_delta = layer1_error * sigmoid_derivative(self.layer1)

        # Обновление весов
        self.weights2 += self.layer1.T.dot(output_delta)
        self.weights1 += self.input.T.dot(layer1_delta)


if __name__ == "__main__":
    # Данные для обучения:

    # Вход: 3 признака
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

    # Ожидаемый выход
    y = np.array([[0], [1], [1], [0]])

    nn = NeuralNetwork(X, y)

    # Обучение:
    # 1. Прямой проход (вычисляем выход)
    # 2. Обратный проход (корректируем веса)
    # Повторяем N раз
    for i in range(int(input("Введите количество итераций для обучения нейросети: "))):
        nn.feedforward()
        nn.backprop()

    # Проверка результата
    print("Ожидаемый результат: ")
    print(y)
    print("Результат после обучения:")
    print(nn.output)
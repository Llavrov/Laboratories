import numpy as np


# Функиця сигмойда
# Необходима для определения значения весов
def sigmoid(x, der=False):
    if der:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения
        # и последующее использование функции активации

        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


# Набор весов
weights = np.array([0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5]).T

# Сделаем  случайные числа более определенными
np.random.seed(1)

# Инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((3, 1)) - 1


bias = 0  # b = 4
n = Neuron(weights, bias)

# Набор входных данных
x = np.array([1, 0, 0, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 1, 0, 0, 1])

# Выходные данные
y = np.array([[1, 0, 0, 1, 1, 0]]).T

# Обцчение нашей нейронки
for iter in range(10000):
    # Прямое распространение
    l0 = x
    l1 = sigmoid(np.dot(l0, weights))

    # Насколько мы ошиблись
    l1_error = y - l1

    # Перемножим это с наклоном сигмоиды
    # на основе значений в l1
    l1_delta = l1_error * sigmoid(l1, True)


print(n.feedforward(x))

# print("Выходные данные после тренировки")
# print(l1)

# if __name__ == '__main__':
#     a = 1
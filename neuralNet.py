import numpy as np

# Функиця сигмойда
# Необходима для определения значения весов
def sigmoid(x, der = False):
    if der:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# Набор входных данных
x = np.array([[1, 0, 0, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0, 1, 0, 1],
              [0, 0, 0, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 1, 0, 0, 1]])

# Выходные данные
y = np.array([[1, 0, 0, 1, 1, 0]]).T

# Сделаем  случайные числа более определенными
np.random.seed(1)

# Инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((8, 1)) - 1

for iter in range(100000):
    # Прямое распространение
    l0 = x
    l1 = sigmoid(np.dot(l0, syn0))

    # Насколько мы ошиблись
    l1_error = y - l1

    # Перемножим это с наклоном сигмоиды
    # на основе значений в l1
    l1_delta = l1_error * sigmoid(l1, True)

    # Обнулим веса
    syn0 += np.dot(l0.T, l1_delta)

print("Выходные данные после тренировки")

for i in range(6):
    if l1 [i][0] > 0.5:
        print("Мне это нравится")
    else:
        print("Не нравится")

"""
Грустный	0.25
Нейтральный	0.25
Веселый	    0.25 
Печальный	0.25
Быстрый	    0.5
Спокойный	0.5
Русс	    0.5
Англ	    0.5
"""


new_one = np.array([0, 1, 0, 0, 0, 1, 1, 0])
l1_new = sigmoid(np.dot(new_one, syn0))
ans = [0, 0, 0, 0, 0, 0, 0, 0]
print("Новые данные: ")
for i in range(3):
    if i == 1:
         print("Жанр: 1. Грустный \n 2. Нейтральный  \n 3. Веселый \n 4. Печальный ")
    elif i == 2:
        print("Темп: 1. Быстрый \n 2. Спокойный ")
    else:
        print("Язык: 1. Русский \n 2. Английский")
    unit = int(input("выберете пункт: "))
    ans[unit] += 1



if l1_new[0] > 0.5:
    print("Мне это нравится")
else:
    print("Не нравится")

# if __name__ == '__main__':
#     a = 1
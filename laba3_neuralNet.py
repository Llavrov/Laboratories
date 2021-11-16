import numpy as np

# Функиця сигмойда
# Необходима для определения значения весов
def sigmoid(x, der=False):
    if der:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


def act(x):
    return 0 if x < 0.5 else 1



def go(house, rock, attr, money, car):

    # Набор входных данных
    x = np.array([[0.3, 0.4, 0, 0 ,0],
                  [0, 0, 1, 0 ,0],
                  [0, 0, 0, 0.4, 0.2]])


    # Выходные данные
    y = np.array([-1, 1, 1])

    units = np.array([house, rock, attr, money, car])

    sum_hidden = np.dot(x, units)       # вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейронах скрытого слоя:  " +str(sum_hidden))

    out_hidden = np.array([act(units) for units in sum_hidden])
    print("Значения на выходах нейронов скрытого слоя:  " +str(out_hidden))

    sum_end = np.dot(y, out_hidden)
    y = act(sum_end)
    print("Выходное значение НС:  " +str(y))

    return y


house = 1
rock = 0
attr = 1
money = 1
car = 0


res = go(house, rock, attr, money, car)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Не сегодня, друг")


# if __name__ == '__main__':
#     a = 1
import numpy as np

a = open('27-A.txt', 'r').read().split('\n')
b = open('27-B.txt', 'r').read().split('\n')

def minSumm(array):
    arraySize = int(array.pop(0))
    min3 = 1000000000
    predmin3 = 1000000000
    ppmin3 = 1000000000
    min2 = 1000000000
    min1 = 1000000000
    for i in range(arraySize):
        item = int(array[i])
        if (item % 3 == 2 and item < min2):
            min2 = item
        if (item % 3 == 1 and item < min1):
            min1 = item
        if (item % 3 == 0):
            if (item < min3):
                ppmin3 = predmin3
                predmin3 = min3
                min3 = item
            elif (item < predmin3):
                ppmin3 = predmin3
                predmin3 = item
            elif (item < ppmin3):
                ppmin3 = item
    if (min1 + min2 > predmin3 + ppmin3):
        return predmin3 + ppmin3 + min3
    return min1 + min2 + min3

print(minSumm(a))
print(minSumm(b))

# if __name__ == '__main__':
#     a = 10



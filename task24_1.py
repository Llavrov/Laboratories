# file = open('zadanie24_2.txt', 'r').read();


def comp(array1, array2):
    if (array1 is None or array2 is None) or (len(array1) != len(array2)):
        return False
    for i in range(len(array1)):
        if array1[i] is not None:
            array1[i] = array1[i] ** 2
        if (array1[i] not in array2):
            return False
        array2[array2.index(array1[i])] = None
    return True



a = []
b = [1]
print(comp(a, b))
# if __name__ == '__main__':
#     a = 10



MatrSize = 4
array = []

for i in range(MatrSize):
    array.append([])

str = input("Введите строку: ")
while len(str) < MatrSize**2:
    str = input("Введите строку длинной 16 символов: ")

next = 0
for i in range(MatrSize):
    for j in range(MatrSize):
        array[i].append(str[next])
        next += 1

print(array)

def rotate(array) -> []:
    tempArray = []
    for i in range(MatrSize):
        tempArray.append([])
    number = 0
    for i in range(0, MatrSize, 2):
        for j in range(0, MatrSize, 2):
            tempArray[number].append(array[i][j])
            tempArray[number].append(array[i][j+1])
            tempArray[number].append(array[i+1][j])
            tempArray[number].append(array[i+1][j + 1])
            number += 1
    return tempArray

result = rotate(array)
ans = ''
for i in range(MatrSize):
    ans += ''.join(result[i])

print(ans)

for i in range(3):
    result = rotate(result)

ans = ''
for i in range(MatrSize):
    ans += ''.join(result[i])

print(ans)
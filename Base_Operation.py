def F(n):
    if n == -1:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * F(n - 2) + F(n - 3)


print(F(6))





if __name__ == '__main__':
    a = 1
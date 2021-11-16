for i in range(2, 100):
    N = 31
    newNum = ''
    more = ['A', 'B', 'C', 'D', 'E', 'F']
    while N > 0:
        if N % i >= 10:
            newNum = more[(N%i)%10] + newNum
            N //= i
        else:
            newNum = str(N % i) + newNum
            N //= i
    if newNum[len(newNum)-2:] == '11':
        print(i)

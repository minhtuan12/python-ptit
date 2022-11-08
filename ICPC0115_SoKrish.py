from math import factorial


def check(n):
    sum = 0
    for i in n:
        sum += factorial(int(i))
    if sum == int(n):
        return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    if check(str(n)):
        print('Yes')
    else:
        print('No')
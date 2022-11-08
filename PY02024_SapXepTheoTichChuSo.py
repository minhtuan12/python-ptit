from functools import cmp_to_key


def mul(n):
    res = 1
    n = str(n)
    for i in n:
        res *= int(i)
    return res

def func(a, b):
    if mul(a) == mul(b):
        if a < b:
            return -1
        elif a > b:
            return 1
    elif mul(a) < mul(b):
        return -1
    return 1
    
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = cmp_to_key(func))
    
    for i in a:
        print(i, end=' ')
    print()
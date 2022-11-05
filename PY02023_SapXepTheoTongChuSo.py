from functools import cmp_to_key


def solve(n):
    sum = 0
    n = str(n)
    for i in n:
        sum += int(i)
    return sum

def func(a, b):
    if solve(a) == solve(b):
        if a < b:
            return 1
        elif a < b: 
            return -1
    elif solve(a) < solve(b):
        return 1
    return -1

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = cmp_to_key(func), reverse=True)
    
    for i in a:
        print(i, end=' ')
    print()
    
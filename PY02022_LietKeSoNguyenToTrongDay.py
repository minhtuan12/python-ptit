from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
used = []

for i in a:
    if i in used:
        continue
    if prime(i):
        print(i, a.count(i))
        used.append(i)
from math import gcd


def check(a, b):
    if gcd(a, b) == 1:
        return True
    return False

n = int(input())
a = sorted([int(x) for x in input().split()])

for i in range(n - 1):
    for j in range(i + 1, n):
        if check(a[i], a[j]):
            print(a[i], end=" ")
            print(a[j])
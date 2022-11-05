from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = [int(x) for x in input().split()]
res = []

for i in range(n):
    a = [int(x) for x in input().split()]
    for j in a:
        if prime(j):
            res.append(1)
        else:
            res.append(0)

cnt = 0
for i in res:
    print(i, end=" ")
    cnt += 1
    if cnt == m:
        print()
        cnt = 0
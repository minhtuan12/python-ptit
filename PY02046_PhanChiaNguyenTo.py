from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [] * n
a = [int(x) for x in input().split()]
b = []

for i in a:
    if b.count(i) == 0:
        b.append(i)
     
res = -1
for i in range(len(b) - 1):
    if prime(sum(b[0:i + 1])) and prime(sum(b[i + 1:])):
        res = i
        break

if res == -1:
    print("NOT FOUND")
else:
    print(res)
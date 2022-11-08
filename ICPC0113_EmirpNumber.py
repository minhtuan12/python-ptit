from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def trans(s):
    rev = ''
    for i in s:
        rev = i + rev
    return rev

t = int(input())
for i in range(t):
    n = int(input())
    res = []
    for i in range(13, n + 1):
        rev = int(trans(str(i)))
        if i != rev:
            if prime(i) and prime(rev):
                if rev < n:
                    if rev not in res:
                        res.append(i)
                        res.append(rev)
    for i in res:
        print(i, end=' ')
    print()

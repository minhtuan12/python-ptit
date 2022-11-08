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

def each(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    return sum

def check(s):
    for i in s:
        if i.isdigit():
            tmp = int(i)
            if not prime(tmp):
                return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if prime(int(s)) and prime(int(trans(s))) and prime(each(s)) and check(s):
        print('Yes')
    else:
        print('No')
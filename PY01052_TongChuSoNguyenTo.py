from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    sum = 0
    for i in s:
        sum += int(i)
    
    if prime(sum):
        return True
    return False    


t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    for i in range(0, len(s)):
        if prime(i) and not prime(int(s[i])) or not prime(i) and prime(int(s[i])):
            return False
    return True


t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
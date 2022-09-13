from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
for i in range(t):
    s = input()
    first, last = "", ""
    
    first += s[:3]
    last += s[-3:]
    
    if prime(int(first)) and prime(int(last)):
        print("YES")
    else:
        print("NO")
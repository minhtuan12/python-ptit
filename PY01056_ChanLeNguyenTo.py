from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    for i in range(0, len(s) - 2, 2):
        if int(s[i]) % 2 != 0:
            return False
    
    for i in range(1, len(s) - 2, 2):
        if int(s[i]) % 2 == 0:
            return False
        
    sum = 0
    for i in s:
        sum += int(i)
    
    if not prime(sum):
        return False
    return True    


t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
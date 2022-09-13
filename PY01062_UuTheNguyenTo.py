from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        
def check(s):
    cnt = 0
    for i in s:
        if prime(int(i)):
            cnt += 1
        else:
            cnt -= 1
    
    if cnt > 0 and prime(len(s)):
        return True
    return False


t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    tmp = int(0)
    for i in range (len(s)):
        tmp += int(s[i])
    if prime(tmp):
        return True
    return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()]
        if check(str(gcd(a, b))):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()

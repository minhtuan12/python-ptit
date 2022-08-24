import math


def prime(a):
    if a < 2:
        return False
    for i in range (2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True

def check(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False


def main():
    t = int(input())
    while t > 0:
        n = int(input())
        k = 0
        for i in range (n):
            if check(i, n):
                k += 1
        if prime(k):
            print("YES")
        else:
            print("NO")
        t -= 1
        
if __name__ == "__main__":
    main()
    
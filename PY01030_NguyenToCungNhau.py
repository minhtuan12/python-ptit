
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n, k = [int(i) for i in input().split()]
    first = int(pow(10, k - 1))
    last = int(pow(10, k))
    cnt = 0
    
    for i in range (first, last):
        if gcd(n, i) == 1:
            print(i, end = " ")
            cnt += 1
            if cnt == 10:
                print()
                cnt = 0

if __name__ == "__main__":
    main()
    
    
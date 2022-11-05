
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    l, r = [int(i) for i in input().split()]
    for a in range(l, r - 1):
        for b in range(a + 1, r):
            for c in range(b + 1, r + 1):
                if gcd(a, b) == 1 and gcd(a, c) == 1:
                    print("(", end="")
                    print(a, end=", ")
                    print(b, end=", ")
                    print(c, end=")")
                    print()
                    
                    
if __name__ == "__main__":
    main()
    
    
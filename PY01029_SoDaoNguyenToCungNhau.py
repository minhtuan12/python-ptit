
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    t = int(input())
    for i in range(t):
        n = input()
        
        rev = ""
        for i in n:
            rev = i + rev
        
        if gcd(int(n), int(rev)) == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
    
    
from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        n = str(n)
        tmp = ""
        for i in range(len(n) - 4, len(n)):
            tmp += n[i]
                
        if prime(int(tmp)):
            print("YES")
        else:
            print("NO")  
            
            
if __name__ == "__main__":
    main()
      
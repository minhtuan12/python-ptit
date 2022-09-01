def check(s):
    s = str(s)
    for i in range(int(len(s) / 2) - 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    
    for i in s:
        if int(i) % 2 != 0:
            return False
    
    if len(s) % 2 != 0:
        return False
    
    return True


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for i in range(2, int(n / 11) + 1):
            tmp = i * 11
            if tmp < n and check(tmp):
                print(tmp, end=" ")
        print() 
            
if __name__ == "__main__":
    main()
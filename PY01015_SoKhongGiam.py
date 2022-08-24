def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()
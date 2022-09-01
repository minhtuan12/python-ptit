def check(s):
    for i in range(len(s) - 2):
        if s[i] != s[i + 2]:
            return False
        if s[i] == s[i + 1]:
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
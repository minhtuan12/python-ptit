def check(s):
    if len(s) < 3:
        return False
    
    pos = int(0)
    for i in range(len(s) - 2):
        if s[i] >= s[i + 1]:
            return False
        if s[i + 1] > s[i] and s[i + 1] > s[i + 2]:
            pos = i + 1
            break
        
    if pos == len(s) - 1:
        return False
    for i in range(pos, len(s) - 1):
        if s[i] <= s[i + 1]:
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
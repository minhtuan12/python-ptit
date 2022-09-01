def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
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
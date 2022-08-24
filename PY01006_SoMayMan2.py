
def check(n):
    for i in n:
        if i != '4' and i != '7':
            return False
    return True

def main():
    t = int(input())
    while t > 0:
        n = str(input())
        if check(n):
            print("YES")
        else:
            print("NO")
        t -= 1

if __name__ == "__main__":
    main()
    

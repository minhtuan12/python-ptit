
def check(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 10 == 0:
        return True
    return False

def nextTo(n):
    for i in range(len(n) - 1):
        if abs(ord(n[i]) - ord(n[i + 1])) != 2:
            return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n = input()
        if check(n) and nextTo(n):
            print("YES")
        else:
            print("NO")
            
if __name__ == "__main__":
    main()
    
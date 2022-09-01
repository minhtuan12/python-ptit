def rev(n):
    if len(n) == 1:
        return n
    
    # reverse a string of digits
    tmp = ""
    for i in n:
        tmp = i + tmp
    
    return tmp


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        while n % 7 != 0:
            n += int(rev(str(n)))
        print(n)
        
if __name__ == "__main__":
    main()
def move(n, first, mid, last):
    if n == 1:
        print(first, "->", last)
    else:
        move(n - 1, first, last, mid)
        move(1, first, mid, last)
        move(n - 1, mid, first, last)


def main():
    n = int(input())
    move(n, 'A', 'B', 'C')
    
    
if __name__ == "__main__":
    main()
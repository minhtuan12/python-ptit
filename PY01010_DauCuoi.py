t = int(input())
for i in range(t):
    n = input()
    length = len(n)
    first = str(n[0] + n[1])
    last = str(n[length - 2] + n[length - 1])
    if int(first) == int(last):
        print("YES")
    else:
        print("NO")
    
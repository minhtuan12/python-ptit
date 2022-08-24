t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    if s[n - 2] == '8' and s[n - 1] == '6':
        print("YES")
    else:
        print("NO")
        
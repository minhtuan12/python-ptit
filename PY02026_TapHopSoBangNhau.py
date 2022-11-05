n, m = [int(x) for x in input().split()]
a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

if a == b:
    print("YES")
else:
    print("NO")

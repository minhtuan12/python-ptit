t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    for i in range(n):
        if a[i] == max(a):
            pos = i
    a.insert(pos, m)
    
    for i in a:
        if i < 0:
            print(i, end=' ')
    for i in a:
        if i >= 0:
            print(i, end=' ')
    print()
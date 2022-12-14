t = int(input())
for i in range(t):
    s = [str(x) for x in input().split()]
    
    sum = 0
    for i in s:
        sum += len(i) + 1
        if sum <= 100:
            print(i, end=' ')
    print()
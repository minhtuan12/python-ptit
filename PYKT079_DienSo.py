t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    tmp = set(a)
    length = max(tmp) - min(tmp) + 1
    print(length - len(tmp))
    
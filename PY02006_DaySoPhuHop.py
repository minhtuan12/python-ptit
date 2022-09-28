def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()]) 
    
    if check(a, b, n):
        print("YES")
    else:
        print("NO") 
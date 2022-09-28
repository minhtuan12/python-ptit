f = [0, 1]
for i in range(2, 93):
    f.append(f[i - 1] + f[i - 2])
    
t = int(input())
for i in range(t):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b + 1):
        print(f[i], end=" ")
    print()
n, k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])

res = 0
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) > k:
        res += 1
        
print(res + 1)
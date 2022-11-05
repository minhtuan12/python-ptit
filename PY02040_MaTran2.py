n = int(input())
a = [[]] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]
    
k = int(input())

sum = 0
for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            sum += a[i][j]
        elif j > n - i - 1:
            sum -= a[i][j]
            
if abs(sum) <= k:
    print("YES")
else:
    print("NO")
print(abs(sum))
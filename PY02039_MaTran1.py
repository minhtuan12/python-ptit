n = int(input())
a = [[]] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]
    
k = int(input())

sum = 0
for i in range(n):
    for j in range(n):
        if i > j:
            sum += a[i][j]
        elif i < j:
            sum -= a[i][j]
            
if abs(sum) <= k:
    print("YES")
else:
    print("NO")
print(abs(sum))
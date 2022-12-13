n, m = [int(x) for x in input().split()]
a = [[] * m] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

cnt = 0
if n > m:
    for i in range(n):
        if (i + 1) % 2 != 0:
            cnt += 1
        if cnt > n - m or (i + 1) % 2 == 0:
            for j in range(m):
                print(a[i][j], end=' ')
            print()
elif n < m:
    for i in range(n):
        cnt = 0
        for j in range(m):
            if (j + 1) % 2 == 0:
                cnt += 1
            if cnt > m - n or (j + 1) % 2 != 0:
                print(a[i][j], end=' ')
        print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()

a, k, n = [int(i) for i in input().split()]
ok = 0
nums = int(n / k)
for i in range (1, nums + 1):
    tmp = int(i * k)
    if tmp > a:
        print(tmp - a, end = " ")
        ok = 1
if ok == 0:
    print(-1)
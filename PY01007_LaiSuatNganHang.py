from math import pow

t = int(input())
while t > 0:
    n, x, m = [float(i) for i in input().split()]
        
    year = float(1)
    tmp = float(n * pow(1 + (x / 100), year))
    while tmp < m:
        year += 1
        tmp = n * pow(1 + (x / 100), year)
    print(int(year))
    t -= 1
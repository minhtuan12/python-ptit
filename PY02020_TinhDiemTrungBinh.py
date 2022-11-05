#-
n = int(input())
a = [float(x) for x in input().split()]

Min = min(a)
Max = max(a)
cntMin, cntMax = 0, 0
summ = 0

for i in a:
    summ += i
    if i == Min:
        cntMin += 1
    if i == Max:
        cntMax += 1
        
print("{:.2f}".format((summ - Min * cntMin - Max * cntMax) / (n - cntMin - cntMax)))
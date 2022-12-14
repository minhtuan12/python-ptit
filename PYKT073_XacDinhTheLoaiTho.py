n = int(input())
tp, a = [], []

sentences = 0
for i in range(n):
    s = input().split()
    if len(s) == 6 and len(a) == 0:
        tp.append(1)
    a.append(s)
    
    if len(a) >= 2 and len(s) == 6 and len(a[-2]) == 7:
        tp.append(1)
        
    if len(s) == 7:
        sentences += 1
        if sentences == 4:
            tp.append(2)
            sentences = 0
    
print(len(tp))
for i in tp:
    print(i)
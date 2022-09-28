a = []
while len(a) < 10:
    for i in input().split():
        a.append(int(i))
    
res = set()
for i in a:
    res.add(i % 42)   
print(len(res))
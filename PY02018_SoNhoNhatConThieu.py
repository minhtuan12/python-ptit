n = int(input())
a = sorted([int(x) for x in input().split()])

tmp = 2
ok = 0

for i in a:
    if i >= 2:
        if i != tmp:
            print(tmp)
            ok = 1
            break
        tmp += 1
        
if ok == 0:
    print(tmp)
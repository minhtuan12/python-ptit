t = int(input())
for i in range(t):
    s = input()
    tmp = []
    sum = 0
    
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            tmp.append(i)
    
    tmp = sorted(tmp)
    for i in tmp:
        print(i, end='')
    print(sum)
def check_done(a):
    for i in range(3):
        if a[i] != a[i + 1]:
            return False
    return True


while True:
    a = [int(i) for i in input().split()]
    
    # exit
    cnt = 0
    for i in range(4):
        if a[i] == 0:
            cnt += 1
    if cnt == 4:
        break
    
    cnt = 0
    while not check_done(a):
        first = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - first)
        cnt += 1
        
    print(cnt)
        
        
    
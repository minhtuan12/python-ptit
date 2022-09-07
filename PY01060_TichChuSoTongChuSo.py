t = int(input())
for i in range(t):
    s = input()
    
    # caculate sum
    sum = 0
    cntOdd = 0
    for i in range(0, len(s)):
        if i % 2 != 0:
            sum += int(s[i])
            cntOdd += 1
    
    # caculate mul
    cntEven = 0
    mul = 1
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                mul *= int(s[i])
            else:
                cntEven += 1
    
    if cntOdd == len(s) - cntEven:
        print(0, end=" ")
    else:
        print(mul, end=" ")
    print(sum)
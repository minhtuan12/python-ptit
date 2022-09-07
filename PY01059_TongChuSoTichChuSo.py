t = int(input())
for i in range(t):
    s = input()
    
    # caculate sum
    sum = 0
    cntEven = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            sum += int(s[i])
            cntEven += 1
    
    # caculate mul
    cntOdd = 0
    mul = 1
    for i in range(1, len(s)):
        if i % 2 != 0:
            if s[i] != '0':
                mul *= int(s[i])
            else:
                cntOdd += 1
    
    print(sum, end=" ")
    if cntOdd == len(s) - cntEven:
        print(0)
    else:
        print(mul)
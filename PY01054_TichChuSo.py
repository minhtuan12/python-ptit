def solve(s):
    mul = 1
    for i in s:
        if i != '0':
            mul *= int(i)
    
    return mul


t = int(input())
for i in range(t):
    s = input()
    print(solve(s))
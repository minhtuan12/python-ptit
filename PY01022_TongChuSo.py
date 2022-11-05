def trans(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    return str(sum)

def solve(s):
    if len(s) == 1:
        return 1
    
    cnt = 0
    while len(s) > 1:
        cnt += 1
        s = trans(s)
    return cnt


s = input()
print(solve(s))
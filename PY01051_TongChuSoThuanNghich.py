def check(s):
    tmp = ""
    for i in s:
        tmp = i + tmp
    if tmp == s:
        return True
    return False


def solve(s):
    sum = 0
    for i in s:
        sum += int(i)
    
    if len(str(sum)) > 1 and check(str(sum)):
        return True
    return False


t = int(input())
for i in range(t):
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")
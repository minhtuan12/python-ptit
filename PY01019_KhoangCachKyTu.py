t = int(input())
for i in range(t):
    s = input()
    rev = ""
    for i in s:
        rev = i + rev
    
    cnt = int(0)
    for i in range (len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) == abs(ord(rev[i]) - ord(rev[i + 1])):
            cnt += 1
    if cnt == len(s) - 1:
        print("YES")
    else:
        print("NO")
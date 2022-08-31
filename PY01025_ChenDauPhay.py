s = input()
rev, tmp  = "", ""
cnt = 0

# reverse s
for i in s:
    rev = i + rev
for i in range (len(rev)):
    tmp += rev[i]
    cnt += 1
    if cnt == 3 and i != len(rev) - 1:
        tmp += ','
        cnt = 0

# reverse again
res = ""
for i in tmp:
    res = i + res
print(res)
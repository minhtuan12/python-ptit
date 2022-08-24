s = input()
cnt = int(0)
for i in range(len(s)):
    if s[i].islower():
        cnt += 1
    elif s[i].isupper():
        cnt -= 1
if cnt >= 0:
    print(s.lower())
else:
    print(s.upper())
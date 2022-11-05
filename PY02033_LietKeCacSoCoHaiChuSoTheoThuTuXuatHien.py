s = input()
a = []
while len(s) >= 2:
    x = s[0] + s[1]
    tmp = int(x)
    a.append(int(x))
    s = s[2:]

tmp = set()
for i in a:
    if i in tmp:
        continue
    print(i, end=' ')
    tmp.add(i)
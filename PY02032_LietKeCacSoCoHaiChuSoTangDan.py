s = input()
a = set()
while len(s) >= 2:
    x = s[0] + s[1]
    a.add(int(x))
    s = s[2:]
a = sorted(a)
for i in a:
    print(i, end=' ')
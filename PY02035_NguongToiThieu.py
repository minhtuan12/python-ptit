s = input()
k = int(input())
a = []

while len(s) >= 2:
    x = s[0] + s[1]
    tmp = int(x)
    a.append(int(x))
    s = s[2:]

ok = False
a = sorted(a)
tmp = set()
for i in a:
    if i in tmp:
        continue
    elif a.count(i) >= k:
        print(i, a.count(i))
        ok = True
        tmp.add(i)
if not ok:
    print("NOT FOUND")
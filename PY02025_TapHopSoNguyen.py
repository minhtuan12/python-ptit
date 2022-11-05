n, m = [int(x) for x in input().split()]
a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

un = sorted(a.intersection(b))

a = sorted(list(a))
b = sorted(list(b))

for i in un:
    a.remove(i)
    b.remove(i)
    print(i, end=" ")
print()

for i in a:
    print(i, end=' ')
print()

for i in b:
    print(i, end=' ')
print()


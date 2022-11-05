def check(a):
    if len(set(a)) == 1:
        return True
    return False

n = int(input())
while n != 0:
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    if check(a):
        print("BANG NHAU")
    else:
        print(min(a), max(a))
    n = int(input())
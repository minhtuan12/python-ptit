t = int(input())
for i in range(t):
    p, q = [str(x) for x in input().split()]
    p = min(p, q)
    q = max(p, q)
    
    s = input().strip()
    if s.count(' '):
        a, b = s.split()
    else:
        a = s
        b = input()
    
    print(int(a.replace(q, p)) + int(b.replace(q, p)), int(a.replace(p, q)) + int(b.replace(p, q)))
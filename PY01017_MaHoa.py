t = int(input())
for i in range(t):
    s = input()
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            print(cnt, end = "")
            print(s[i], end = "")
            cnt = 1
        else:
            cnt += 1
    print(cnt, end = "")
    print(s[len(s) - 1], end = "")
    print(end = "\n")
a = input()
b = input()
idx = int(input())

print(a[0:idx - 1] + b[idx - 1:] + a[idx - 1:])
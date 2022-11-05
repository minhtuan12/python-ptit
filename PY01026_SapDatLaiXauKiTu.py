t = int(input())
for i in range(t):
    a = input()
    b = input()
    a = (sorted(a))
    b = (sorted(b))
    
    print("Test " + f"{i + 1}" + ": ", end="")
    if a == b:
        print("YES")
    else:
        print("NO") 
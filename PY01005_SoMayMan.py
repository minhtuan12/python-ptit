n = str(input())
cnt4 = 0
cnt7 = 0

for i in n:
    if i == '4':
        cnt4 += 1
    elif i == '7':
        cnt7 += 1
        
sum = cnt4 + cnt7
if sum == 4 or sum == 7:
    print("YES")
else:
    print("NO")

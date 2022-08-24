
P = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '.']

while True:
    inp = input()
    if inp == "0":
        break
    tmp, s = inp.split()
    k = int(tmp)
    string = ""
    for i in s:
        idx = P.index(i)
        string += P[(idx + k) % 28]
        
    #reverse string
    res = ""
    for i in string:
        res = i + res
    print(res)
            
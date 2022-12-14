with open('SOTAY.txt') as file:
    lines = file.readlines()

date, s = '', ''
with open('DIENTHOAI.txt', 'w') as op:
    i = 0
    while i < len(lines) - 1:
        if lines[i][5].isdigit():
            date = lines[i][5:]
            s = lines[i + 1].strip() + ': ' + lines[i + 2].strip() + ' ' + date
            op.write(s)
            i += 3
        else:
            s = lines[i].strip() + ': ' + lines[i + 1].strip() + ' ' + date
            op.write(s)
            i += 2


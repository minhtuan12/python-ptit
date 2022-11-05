class Stu:
    def __init__(self, name, birth, p1, p2, p3):
        self.name = name
        self.birth = birth
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def outp(self):
        print('{} {} {:.1f}'.format(self.name, self.birth, self.p1 + self.p2 + self.p3))


a = []
for i in range(5):
    tmp = input()
    a.append(tmp)
stu = Stu(str(a[0]), str(a[1]), float(a[2]), float(a[3]), float(a[4]))
stu.outp()
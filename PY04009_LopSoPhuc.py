class Complex:
    def __init__(self, real, vir):
        self.real = real
        self.vir = vir
    
    def C(self, a):
        tmp, res = Complex(0, 0), Complex(0, 0)
        tmp.real = self.real + a.real
        tmp.vir = self.vir + a.vir
        res.real = tmp.real * self.real + (-1) * tmp.vir * self.vir
        res.vir = tmp.real * self.vir + tmp.vir * self.real
        if res.vir >= 0:
            print('{} + {}i'.format(res.real, res.vir), end=', ')
        else:
            print('{} - {}i'.format(res.real, (-1) * res.vir), end=', ')
    
    def D(self, a):
        tmp, res = Complex(0, 0), Complex(0, 0)
        tmp.real = self.real + a.real
        tmp.vir = self.vir + a.vir
        res.real = tmp.real * tmp.real + (-1) * tmp.vir * tmp.vir
        res.vir = 2 * tmp.real * tmp.vir
        if res.vir >= 0:
            print('{} + {}i'.format(res.real, res.vir))
        else:
            print('{} - {}i'.format(res.real, (-1) * res.vir))


t = int(input())
for i in range(t):
    arr = input().split()
    a = Complex(int(arr[0]), int(arr[1]))
    b = Complex(int(arr[2]), int(arr[3]))
    a.C(b)
    a.D(b)
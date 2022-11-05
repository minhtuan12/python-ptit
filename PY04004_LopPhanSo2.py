from math import gcd


class Frac:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def plus(self, a):
        res = Frac(1, 1)
        res.numer = self.numer * a.denom + self.denom * a.numer
        res.denom = a.denom * self.denom
        
        tmp = gcd(res.numer, res.denom)
        res.numer /= tmp
        res.denom /= tmp
        print(int(res.numer), int(res.denom), sep = '/')
        
arr = input().split()
a = Frac(int(arr[0]), int(arr[1]))
b = Frac(int(arr[2]), int(arr[3]))
a.plus(b)
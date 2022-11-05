from math import gcd


class Frac:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def solve(self):
        tmp = gcd(self.numer, self.denom)
        self.numer /= tmp
        self.denom /= tmp
        print(int(self.numer), int(self.denom), sep = '/')
        
arr = input().split()
a = Frac(int(arr[0]), int(arr[1]))
a.solve()
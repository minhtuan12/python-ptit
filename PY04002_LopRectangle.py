class Rec:
    def __init__(self, a, b, co):
        self.a = a
        self.b = b
        self.co = co[0:1].upper() + co[1:].lower()
    
    def check(self):
        if self.a <= 0 or self.b <= 0:
            return False
        return True
    
    def outp(self):
        if not self.check():
            print("INVALID")
        else:
            print((self.a + self.b) * 2, (self.a * self.b), self.co, sep = ' ')


arr = input().split()
r = Rec(int(arr[0]), int(arr[1]), arr[2])
r.outp()
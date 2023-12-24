class puls:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def cululate(self):
         g = self.a + self.b 
         print("%d"%g)
a = int(input("put your number/n"))
b = int(input("put your number/n"))
q = puls(a,b)
q.cululate()

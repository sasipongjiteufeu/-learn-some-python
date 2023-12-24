class Make_mean:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def Mean(self):
        anw = (self.a+ self.b+ self.c+self.d)/4
        print(anw)

x1,x2,x3,x4 =  input("enter value x1,x2,x3,x4 ->").split("/")
print("x1 = ",x1)
print("x1 = ",x2)
print("x1 = ",x3)
print("x1 = ",x4)

x11 = int(x1)
x22 = int(x2)
x33 = int(x3)
x44 = int(x4)

mean = Make_mean(x11,x22,x33,x44)
mean.Mean()
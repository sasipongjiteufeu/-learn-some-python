import math
class Coner:
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def cone(self):
        volume = 1/3*(math.pi*self.r**2*self.h)
        print(volume)

a = float(input("กรุณาใส่ค่ารัศมี :"))
b = float(input("กรุณาใส่ค่าความสูง :"))
Q = Coner(a,b)
Q.cone()
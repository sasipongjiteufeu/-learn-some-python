import math
class Area:
    def __init__(self , a , b , c):
        self.A = a
        self.B = b
        self.C = c
    def Triangle(self):                                         #ฟังชัน สูตรสามเหลียม
        s = (self.A + self.B + self.C)/2                        #หา S สูตรสามเหลียมด้านไม่เท่า
        area = math.sqrt(s*(s-self.A)*(s-self.B)*(s-self.C))                   #สูตรสามเหลียมด้านไม่เท่า
        print(area)

a = float(input("ค่า 1: "))                                      #รับค่า a , b , c 
b = float(input("ค่า 2: "))                         
c = float(input("ค่า 3: "))

Q = Area(a,b,c)
Q.Triangle()

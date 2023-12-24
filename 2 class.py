import math
class Area:     
    def nonTriangle(self,a,b,c): #ฟังชัน สูตรสามเหลียม
        self.A = a
        self.B = b
        self.C = c
        s = (self.A + self.B + self.C)/2                                        #หา S สูตรสามเหลียมด้านไม่เท่า
        area = math.sqrt(s*(s-self.A)*(s-self.B)*(s-self.C))                    #สูตรสามเหลียมด้านไม่เท่า
        print("nonTriangle = %.2f"%area)
    def Square(self,a,b):
        self.A = a                          #ยาว
        self.B = b                          #กว้าง
        area = self.A * self.B
        print("Square = %.2f"%area)
    def Triangle(self,a,b):
        self.A = a                          #สูง
        self.B = b                          #ฐาน
        area = 0.5*self.A * self.B
        print("Triangle = %.2f"%area)
    def circle(self,r):
        self.R = r
        area = math.pi*self.R**2
        print("circle = %.2f"%area)
Q = Area()
Q.nonTriangle(5,4,6)
Q.Square(5,6)
Q.Triangle(6,5)
Q.circle(8)
import math 

a = int(input("ใส่ค่า a"))
b = int(input("ใส่ค่า b"))
c = int(input("ใส่ค่า c"))
x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
x2 = (-b - math.sqrt(abs(b**2 - 4*a*c)))/2*a
print("%d,%d"%(x1,x2))

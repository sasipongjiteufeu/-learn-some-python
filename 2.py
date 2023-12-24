import math

def Triangle(s1,s2,s3):                         #ฟังชัน สูตรสามเหลียม
    s = (s1 + s2 + s3)/2                        #หา S สูตรสามเหลียมด้านไม่เท่า
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))    #สูตรสามเหลียมด้านไม่เท่า
    print(area)

a = float(input("ค่า 1: "))                      #รับค่า a , b , c 
b = float(input("ค่า 2: "))                         
c = float(input("ค่า 3: "))

Triangle(a,b,c)                                 # นำ a , b , c ใส่ไปในฟังชัน

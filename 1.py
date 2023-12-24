import math

s1 = float(input("ค่า 1: "))
s2 = float(input("ค่า 2: "))
s3 = float(input("ค่า 3: "))

s = (s1 + s2 + s3)/2

area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)
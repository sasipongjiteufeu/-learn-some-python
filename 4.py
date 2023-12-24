class make_time:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def Time(self):
        print("Current time = %02d:%02d:%02d"%(self.a,self.b,self.c))
    
a = int(input("Enter current hour:"))
b = int(input("Enter current minute:"))
c = int(input("Enter current second:"))

time = make_time(a,b,c)
time.Time()
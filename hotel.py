class Hotal_offset:
    def __init__(self,city):
        self._city = city 
    def Area_collecter_system(self): # เช็คห้อง
        Area = ["กรุงเทพ","เชียงราย","เชียงใหม่","ภูเก็ต","กระบี่","ชุมพร"]
        if self._city in Area: 
            return self._city   # ส่งค่าออกนอก
        else:
            print("/nSomething is wrong. please check your input and try again.")

class Hotal_room(Hotal_offset): # subclass ของ Hotal_offset
    def __init__(self,room,bed,food):
        super().__init__(self)  # เรียกใช้ constructor ของ superclass
        self._bed = bed
        self._room = room
        self.food = food
        
    def room_collecter_system(self): # เช็คห้อง
        Room = ['A','B','C'] # A = ห้องชมวิว B = ห้องเงียบสงบ C = แบบครอบครัว
        self.room = input("Input your type room : \n")
        if self._room in Room:
            return self._room # ส่งค่าห้องออกนอก
        else:
            print("/nSomething is wrong. please check your input and try again.") 
       
    def bed_collecter_system(self): # เช็คเตียง
        Bed = ['S','M'] # เตียง S = เดียว, เตียง M = คู่
        self.bed = input("Input your type bed : \n")
        if self._bed in Bed:
            return self._bed # ส่งค่าห้องออกนอก
        else:
            print("/nSomething is wrong. please check your input and try again.")
    def food_collecter_system(self): # เช็คอาหาร
        Food = ['Y','N'] # Y เอาอาหาร N ไม่เอาอาหาร
        self._food = input("Input your type food : \n")
        if self._food in Food:
            return self._food # ส่งค่าห้องออกนอก
        else:
            print("/nSomething is wrong. please check your input and try again.")
castomer = []
castom = Hotal_room
print("มีสาขา กรุงเทพ,เชียงราย,เชียงใหม่,ภูเก็ต,กระบี่,ชุมพรn \n")
print(f"โปรดเลือกมาหนึ่งสาขา-> {castom.Area_collecter_system()}")
print("ห้องที่คุณต้องการโดยพิมพ์ตัวอักษร : A ห้องชมวิว B ห้องเงียบสงบ C แบบครอบครัว\n")
print(f"โปรดเลือกห้อง-> {castom.room_collecter_system()}")
print("ห้องที่คุณต้องการอยากได้เตียงแบบใด พิมพ์ตัวอักษร S = เดียว M = คู่\n")
print(f"โปรดเลือกเตียง-> {castom.bed_collecter_system()}")
print("ท่านต้องการอาหารหรือไม่\n")
print(f"โปรดเลือก-> {castom.food_collecter_system()}")





import os
from time import sleep
class E_com :
    def __init__(self,User,passwod,User_address,Phone_number,money_in_app):
        self._User = User
        self._passwod = passwod
        self.User_address = User_address
        self.Phone_number = Phone_number
        self._money_in_app =  money_in_app
        
    def Login_in_app(self):
        __passwod =  '123456'
        __Username = 'beermini991'
        max_attempts = 3
        for attempt in range(max_attempts):
            print("************ได้โปรดล็อคอิน************")
            self.User = input("User name :")
            self.passwod = input("passwond :")
            if self.User == __Username and self.passwod == __passwod:
                print("<<<<<<<<รหัสผ่านถูกต้อง>>>>>>>")
                os.system('cls')
                break
            else:
                print("-----------ได้โปรดลองใหม่------------")
                print("reset in 5 sec")
                sleep(6)
                os.system('cls')
        if attempt == max_attempts:
            print("+++++++คุณได้พิมพ์เกิน 3 ครั้งกรุณาลองใหม่ภายหลัง+++++++")
            
    def q_phone_nunber(self):
            print("*************ได้โปรดใส่เบอร์โทรศัพท์ของคุณ*************")
            self.Phone_number = input("Phone number->")
            return self.Phone_number 
    def ark_address(self):
            self.User_address = input("Your address->")
            return self.User_address
class Item_shop_and_buy(E_com):
    def __init__(self,User,passwod,User_address,Phone_number,money_in_app,oder):
        super().__init__(User,passwod,User_address,Phone_number,money_in_app)
        self._oder = oder
    def colloat_oder(self):
        self.money_in_app = 50000
        item = ['รองเท้า','โน๊ตบุ๊ก','โทรศัพท์','เมาส์']
        prirn = [1500,20000,6000,400]
        print("///////ได้โปรดใส่เลขสินค้าที่ต้องการ///////")
        print("1.รองเท้า")
        print("2.โน๊ตบุ๊ก")
        print("3.โทรศัพท์")
        print("4.เมาส์")
        self._oder = int(input("------>"))
        max_attempts = 3
        for attempt in range(max_attempts):
            if self._oder == int:
                print(f"คุณได้เลือก {item[self._oder - 1]}")
                break
            elif(self._oder != int):
                print("////ลองอีกครั้ง////")
        if attempt == max_attempts:
            print("+++++++คุณได้พิมพ์เกิน 3 ครั้งกรุณาลองใหม่ภายหลัง+++++++")
            
        print ("-------------------------------")
        print (f"ราคาเท่ากับ{prirn[self._oder-1]}")
        print (f"เงินที่ท่านมีคือ{self.money_in_app}")
        print ("-------------------------------")
        print ("-------------------------------")
        print (f"เงินที่ท่านคงเหลือคือ{self.money_in_app-prirn[self._oder-1]}")
        
    def charck_address(self):
        print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
        print("ได้โปรดเช็คที่อยู่และเบอร์ของท่านอีกครั้ง")
        print(f"{self.User_address} เบอร์:{self.Phone_number}")
        print("ใช้ไหมครับ? Y/N")
        chosion = input("------->")
        if chosion == 'Y':
            print("***********ธุรกรรมเสร็จสิ้น***********")
        elif chosion == 'N':
            print("............ได้โปรดกรอกที่อยู่ใหม่อีกครั้ง............")
            self.User_address = input("ที่อยู่: ")
            self.Phone_number = input("เบอร์โทร: ")
            print("----------------------------------------------------")
            print(f"ที่อยู่:{self.User_address}เบอร์โทร:{self.Phone_number}")
            print("0.0.0.0.0.0. ธุรกรรมเสร็จสิ้น 0.0.0.0.0.0.")

U = E_com(None,None,None,None,None)
U.Login_in_app()
gg = U.q_phone_nunber()
ggv2 =U.ark_address()
z = Item_shop_and_buy(None,None,ggv2,gg,None,None)
z.colloat_oder()
z.charck_address()
            
        
        
        

        
    
        
                
        
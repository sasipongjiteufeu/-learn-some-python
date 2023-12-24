class four_back:
    def __init__(self,ID):
        self.ID = ID
    def ID_num(self):
        a = self.ID[-4:]
        print(a)
    
id = input(">")
Q = four_back(id)
Q.ID_num()
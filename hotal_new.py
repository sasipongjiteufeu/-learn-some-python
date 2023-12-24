class Hotel:
    def __init__(self, city):
        self._city = city

    def area_collector_system(self):
        areas = ["กรุงเทพ", "เชียงราย", "เชียงใหม่", "ภูเก็ต", "กระบี่", "ชุมพร"]
        if self._city in areas:
            return self._city
        else:
            print("\nSomething is wrong. Please check your input and try again.")

class HotelRoom(Hotel):
    def __init__(self, city, room, bed, food):
        super().__init__(city)
        self._bed = bed
        self._room = room
        self._food = food

    def room_collector_system(self):
        rooms = ['A', 'B', 'C']
        self._room = input("Input your room type (A, B, C): ")
        if self._room in rooms:
            return self._room
        else:
            print("\nSomething is wrong. Please check your input and try again.")

    def bed_collector_system(self):
        beds = ['S', 'M']
        self._bed = input("Input your bed type (S, M): ")
        if self._bed in beds:
            return self._bed
        else:
            print("\nSomething is wrong. Please check your input and try again.")

    def food_collector_system(self):
        food_options = ['Y', 'N']
        self._food = input("Do you want food (Y/N): ")
        if self._food in food_options:
            return self._food
        else:
            print("\nSomething is wrong. Please check your input and try again.")
            
            
print("Available cities: กรุงเทพ, เชียงราย, เชียงใหม่, ภูเก็ต, กระบี่, ชุมพร\n")
customer = []
custom = HotelRoom(input("Enter your selected city: "), None, None, None)


selected_city = custom.area_collector_system()
print(f"You selected the city: {selected_city}")

print("Room types: A (ห้องชมวิว), B (ห้องเงียบสงบ), C (แบบครอบครัว)\n")
selected_room = custom.room_collector_system()
print(f"You selected room type: {selected_room}")

print("Bed types: S (เตียงเดียว), M (เตียงคู่)\n")
selected_bed = custom.bed_collector_system()
print(f"You selected bed type: {selected_bed}")

print("Food options: Y (เอาอาหาร), N (ไม่เอาอาหาร)\n")
selected_food = custom.food_collector_system()
print(f"You selected food option: {selected_food}")


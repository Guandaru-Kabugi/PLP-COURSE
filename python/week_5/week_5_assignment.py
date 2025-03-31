class Smartphone:
    def __init__(self,brand,model,storage,battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self._battery_life = battery_life #encapusaltion
    
    def get_battery_life(self):
        return f"Battery life is: {self._battery_life} hours"
    def charge(self):
        return "charging now..."
    def __str__(self):
        return f"{self.brand} {self.model} - {self.storage}GB."
    
#inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def boost_performance(self):
        return f"performance boosted to enhance gaming"
    def __str__(self):
        return super().__str__() + f" | Gaming Mode: {self.cooling_system} cooling."
    
phone1 = Smartphone("Samsun","Galaxy S22", 512,100)
phone2 = GamingPhone("Apple","Iphone 14",128,80,"Liquid")

print(phone1)
print(phone2)
print(phone1.get_battery_life())
print(phone1.charge())
print(phone2.boost_performance())


#Task 2
class Plane:
    def __init__(self):
        pass
    def move(self):
        return "Flying...."
class Car:
    def __init__(self):
        pass
    def move(self):
        return "Driving..."
class Dog:
    def __init__(self):
        pass
    def move(self):
        return "Running..."
    

for element in [Plane(),Car(),Dog()]:
    print(element.move())
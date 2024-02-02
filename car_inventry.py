class car:
    def __init__(self,model,make,year,price):
        self.model=model
        self.make=make
        self.year=year
        self.price=price
        self.available=True

    def display_model(self):
        print(f"{self.model},
        {self.make},
        {self.year},
        {self.price},
        {self.available}")

class dealership:
    def __init__(self,name):
          self.name = name
          self.inventory = []

    def add_car_to_inventry(self,car):
        self.inventry.append(car)

    def display_available_car(self):
        available_cars = [car.display_info() for car in self.inventory if car.available]
        return "Available Cars:\n" + "\n".join(available_cars)

    def sell_car(self, customer, car_index):
        if 0 <= car_index < len(self.inventory) and self.inventory[car_index].available:
            car = self.inventory.pop(car_index)
            customer.purchase_car(car)
            return car
        else:
            return None

class customer:
    def __init__(self,name):
        self.name=name
        self.purchased=[]
    def purchase_car(self, car):
        self.purchased.append(car)
        car.available = False


#creating objects 
        
car1 = car("maruti suzuki","camy",2022,25000)
car2 = car("ford","camy",2022,4343434)
car3= car("brezza","camy",2022,4343434)

dealership = dealership("ABC Motors")
dealership.add_car_to_inventory(car1)
dealership.add_car_to_inventory(car2)
dealership.add_car_to_inventory(car3)

customer1 = customer("John Doe")

print(dealership.display_available_cars())

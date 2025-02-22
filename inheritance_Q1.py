# Write a python program to create a class vehicle with attributes brand & price.
# derive a class car from it & add an addition attribute fuel_type. implement a constructor & a display function.

class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

class Car(Vehicle):
    def __init__(self, brand, price, fuel_type):
        super().__init__(brand, price)
        self.fuel_type = fuel_type

    def display(self):
        super().display()
        print(f"Fuel Type: {self.fuel_type}")

car = Car("BMW", 2000000, "Petrol")
car.display()

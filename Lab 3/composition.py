# Q5. Composition
# Create a class called Engine with attributes:
# fuel_type (e.g., "petrol", "diesel", "electric")
# horsepower
# Modify the Car class to include an Engine object as an attribute. Update the Car class's
# __init__ method to accept an Engine object.
# Create a Car instance with an Engine and test its functionality.

class Engine:
    def __init__(self, fuel, horsepower):
        self.fuel = fuel
        self.horsepower = horsepower
    
    def __str__(self):
        return f"Engine: {self.fuel}, {self.horsepower} HP"

class Car:
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self.engine = engine 

    def display_info(self):
        return f"Car: {self.brand}, {self.color}, {self.engine}"
engine = Engine("petrol", 200)

car = Car("Nissan", "Black", engine)
print(car.display_info())

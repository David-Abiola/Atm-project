# Student Management System
#
# https://my-first-web-ieje.onrender.com/
# What to build
#
# Add students
#
# View students
#
# Update scores
#
# Calculate average & grade
#
# Classes

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("vehicle is starting")
    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, wheels):
        super().__init__(brand, model, year)
        self.doors = doors
        self.wheels = wheels

class Bike(Vehicle):
    def __init__(self,brand ,model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels
car = Car("lexus", "dorf", 2022, 4, 4)
bike = Bike("honda", "sst", 2018, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()



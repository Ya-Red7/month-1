# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.__make = make   
        self.__model = model 

    def describe(self):
        return f"Vehicle Make: {self.__make}, Model: {self.__model}"
    
    # Getters
    def get_make(self): 
        return self.__make
    def get_model(self):  
        return self.__model

# Subclasses

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):  # Overriding the describe() method
        return f"Car Make: {self.get_make()}, Model: {self.get_model()}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def describe(self):  
        return f"Bike Make: {self.get_make()}, Model: {self.get_model()}"

# Polymorphism example
def printDescription(vehicle):
    print(vehicle.describe())


# Creating objects
car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "R15")


printDescription(car)  
printDescription(bike) 

class Vehicle:
    def vehicleDetails(self,brand,speed):
        self.brand=brand
        self.speed=speed

class Car(Vehicle):
    def carDetails(self):
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)

class Bike(Vehicle):
    def bikeDetails(self):
        print("Brand: ",self.brand)
        print("Speed: ",self.speed)

car1=Car() 
bike1=Bike() 

car1.vehicleDetails("Lambhorgini",180)
bike1.vehicleDetails("Royal Enfield",160)

car1.carDetails()
bike1.bikeDetails()

class product:
    def productDetails(self,name,price):
        self.name=name
        self.price=price
class ElectronicProduct(product):
    def electronicDetails(self,brand,warranty):
        self.brand=brand
        self.warranty=warranty
class MobilePhone(ElectronicProduct):
    def displayDetails(self):
        print("Product Name: ",self.name)
        print("Price: ",self.price)
        print("Brand: ",self.brand)
        print("warranty in years: ",self.warranty)
p1=MobilePhone()

p1.productDetails("smartphone",45000)
p1.electronicDetails("vivo y21",1)
p1.displayDetails()




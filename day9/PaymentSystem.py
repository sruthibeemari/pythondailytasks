class payment:
    def processPayment(self):
        print("Processsing payment")
class creditCard(payment):
    def processPayment(self):
        print("Proccesing payment through Credit Card")
class UPI(payment):
    def processPayment(self):
        print("Proccesing payment through UPI")
class NetBanking(payment):
    def processPayment(self):
        print("Proccesing payment Net Banking")

p1=creditCard()
p1.processPayment()
p2=UPI()
p2.processPayment()
p3=NetBanking()
p3.processPayment()

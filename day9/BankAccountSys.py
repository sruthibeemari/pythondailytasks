class BankAccount:
    def __init__(self,Account_Number,Balance):
        self.Account_Number=Account_Number
        self.Balance=Balance
    
    def deposit(self,amount):
        self.Balance+=amount
        print("Amount Deposited: ",amount)


    def withdraw(self,amount):
        if amount>self.Balance:
            print("insufficient Balance")
        else:
            self.Balance-=amount
            print("amount withdrawn Successfully",amount)
    
    def displayBalance(self):
            print("Account Number: ",self.Account_Number)
            print("Balance: ",self.Balance)



account1=BankAccount(1000901,3000)
account1.deposit(1000)
account1.withdraw(1500)
account1.displayBalance()


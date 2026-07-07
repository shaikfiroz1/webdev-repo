# class BankAccount :
#     bank_name = "SBI" 


#     def __init__(self, owner_name, balance):
        
#         self.owner_name = owner_name

#         self.balance = balance 

#     def deposit(self , amount):
        
#         if amount >=0 :
#             self.balance += amount 
        
#         else :
#             print ("Invalid amount")

#     def __str__(self):
       
#        return f"Owner : {self.owner_name} | Balance : {self.balance}, Bank : {BankAccount.bank_name} "
    
# account = BankAccount("Firoz", 10000)

# account.deposit(2000)

# print(account)

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal Successful")
#         else:
#             print("Insufficient Balance")


# account = BankAccount(1000)

# account.withdraw(200)

# print(account.balance)

# class Wallet:    
#     balance = 0 
# w1 = Wallet()
# w2 = Wallet()
# w1.balance = 500
# Wallet.balance = 1000
# print(w1.balance, w2.balance)

# Write a class `StockPosition` with attributes `symbol`, `quantity`, and `avg_price`. 
# Create three objects representing three different stock positions and print each one's total invested value (quantity × avg_price) using a loop.


class StockPosition :

    def __init__(self, symbol, quantity, avg_price):

        self.symbol = symbol
        self.quantity= quantity
        self.avg_price = avg_price

    def total(self):
        print( self.quantity*self.avg_price )


account1 = StockPosition("S", 2,3)
account2 = StockPosition("B", 2,4)     
account3 = StockPosition("N", 2,5)  


positions = [account1, account2,account3]


for pos in positions :

    pos.total()

    

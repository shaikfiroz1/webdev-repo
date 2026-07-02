# class TradingAccount:

#     def __init__(self, trader_name, capital):

#         self.trader_name = trader_name
#         self.capital = capital

#     def add(self , profit ) :
#             self.capital +=profit




# firozAccount = TradingAccount("Firoz", 100000)

# firozAccount.add(300)

# print (firozAccount.capital)




class TradingAccount: 
    @staticmethod
    def calculate_brokerage(amount) :
        return (amount/100) *2 
    
print(TradingAccount.calculate_brokerage(200))
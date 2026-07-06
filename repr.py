class TradingAccount :

    def __init__(self ,trader_name,capital):
          
        self.trader_name= trader_name
        self.capital = capital 
    
    def __str__(self):
         return  f"Trader = {self.trader_name} | capital = {self.capital}"
    
    def __repr__(self):
         return f"TradingAccount {self.trader_name,self.capital }"
    

account = TradingAccount("Firoz", 150000)

print(account)

print([account])



     
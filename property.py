class TradeAccount :

    def __init__(self):
        self.__capital=100000

    @property
    def  Return__capital(self) :
        return self.__capital  

    @Return__capital.setter
    def Return__capital(self , amount)  :
        if 0 <= amount:
         self.__capital = amount 
        else :
         print("Invalid capital")
account = TradeAccount()

print(account.Return__capital)

account.Return__capital = 150000

print(account.Return__capital)

account.Return__capital = -500

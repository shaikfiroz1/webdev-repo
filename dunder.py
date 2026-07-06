class TradingAccount:

    def __init__(self, trader_name, capital):
        self.__trader_name=trader_name
        self.__capital = capital

    def __str__(self):
        return f"Trader = {self.__trader_name} | capital = {self.__capital}"

account = TradingAccount("Firoz", 150000)

print(account)   
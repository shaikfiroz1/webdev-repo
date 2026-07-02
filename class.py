class TradingAccount:
    market ="NSE"
    @classmethod
    def change_market(cls, market):
        cls.market= market
TradingAccount.change_market("BSE")
print (TradingAccount.market)
class portfolio:
    exchange = "NSE"

    def __init__(self, investor_name, portfolio_value):

        self.investor_name=investor_name
        self.portfolio_value=portfolio_value

investor1=portfolio("Firoz", 150000)
investor2 = portfolio("Rahul", 80000)



print(investor1.portfolio_value)
print(investor2.portfolio_value)
print(investor1.exchange)
print(investor2.exchange)

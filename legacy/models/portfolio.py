from models.stock import StockType

class Portfolio:
    username = 'Unavailable'
    value = 0
    total_value = 0
    stocks = []

    def __init__(self) -> None:
        pass

    def get_total_return(self):
        total_return = 0
        for stock in self.stocks:
            total_return += stock.return_value
        return total_return
    
    def get_base_portfolio_value(self):
        total_base_value = 0
        for stock in self.stocks:
            total_base_value += stock.get_base_value()
        return total_base_value

    def get_total_return_percentage(self):
        total_return = self.get_total_return()
        return total_return / (self.value - total_return)

    def get_stock_portfolio_percentage(self, stock):
        return stock.total_value / self.value

    def get_free_cash(self):
        return self.total_value - self.value

    def get_picks(self):
        return [stock for stock in self.stocks if stock.stock_type == StockType.STOCK]

    def get_etfs(self):
        return [stock for stock in self.stocks if stock.stock_type == StockType.ETF]
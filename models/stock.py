class OwnedStock:
    ticker = 'N/A'
    name = 'Unavailable'
    quantity = 0
    total_value = 0
    return_value = 0
    stock_type = 'N/A'
    logo_url = ''

    def __init__(self, ticker, name, quantity, total_value, return_value, stock_type, logo_url):
        self.ticker = ticker
        self.name = name
        self.quantity = quantity
        self.total_value = total_value
        self.return_value = return_value
        self.stock_type = stock_type
        self.logo_url = logo_url

    def get_base_value(self):
        return self.total_value - self.return_value
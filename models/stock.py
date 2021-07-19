from util.currency import remove_currency_signs

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
    
    def get_return_percentage(self):
        return self.return_value / self.get_base_value()

def get_stocks_list(driver):
    print('Getting investments...')
    investments_section = driver.find_element_by_class_name('investments-section')
    
    # Faster than getting elements one by one inside a for loop
    stock_tickers = [item.get_attribute('innerHTML') for item in investments_section.find_elements_by_class_name('instrument-logo-name')] # TICK
    stock_names = [item.text for item in investments_section.find_elements_by_class_name('text')] # Stock Name
    stock_quantities = [float(item.text.split(' ')[0]) for item in investments_section.find_elements_by_class_name('quantity')] # 0.00000 shares
    stock_total_values = [float(remove_currency_signs(item.text)) for item in investments_section.find_elements_by_class_name('total-value')] # $123.45
    stock_return_values = [float(remove_currency_signs(item.find_element_by_tag_name('div').text.split(' ')[0])) for item in investments_section.find_elements_by_class_name('return')] # $-123.45 (-0.00%)
    stock_types = ['Stock' if item.get_attribute('data-qa-item').count('_') == 2 else 'ETF' for item in investments_section.find_elements_by_class_name('investment-item')] # TICK_US_EQ | TICK_EQ
    stock_logo_urls = [item.get_attribute('src') for item in investments_section.find_elements_by_tag_name('img')] # link

    owned_stocks = []
    for i in range(len(stock_tickers)):
        owned_stock = OwnedStock(
            stock_tickers[i],
            stock_names[i],
            stock_quantities[i],
            stock_total_values[i],
            stock_return_values[i],
            stock_types[i],
            stock_logo_urls[i]
        )

        owned_stocks.append(owned_stock)
    
    return owned_stocks
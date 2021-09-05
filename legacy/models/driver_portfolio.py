from models.portfolio import Portfolio

from models.stock import d_get_stocks_list
from util.currency import remove_currency_signs

class DriverPortfolio(Portfolio):

    def __init__(self, driver):
        if d_is_trading_type_real(driver):
            self.username = d_get_username(driver) 
            self.value = d_get_portfolio_value(driver)
            self.total_value = d_get_portfolio_total_value(driver)
            self.stocks = d_get_stocks_list(driver)
        else:
            print('Investing type is Demo, please login in your browser manually and change to Investing first')

def d_get_portfolio_value(driver):
    print('Getting portfolio value...')
    portfolio_value_section = driver.find_element_by_class_name('portfolio-value')
    portfolio_values = portfolio_value_section.find_elements_by_class_name('formatted-price-part')

    portfolio_value_str = ''
    for elem in portfolio_values:
        portfolio_value_str += elem.text

    return float(remove_currency_signs(portfolio_value_str))

def d_get_portfolio_total_value(driver):
    return float(remove_currency_signs(driver.find_element_by_class_name('account-status-header-value').text))

def d_get_username(driver):
    print('Getting username')

    return driver.find_element_by_class_name('username').text

def d_is_trading_type_real(driver):
    return driver.find_element_by_class_name('trading-type').text.lower() == 'Investing - Real Money'.lower()
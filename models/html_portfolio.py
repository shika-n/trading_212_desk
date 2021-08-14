from models.portfolio import Portfolio
from models.stock import h_get_stocks_list
from util.currency import remove_currency_signs

class HtmlPortfolio(Portfolio):

    def __init__(self, soup):
        print('From parsed HTML file')
        if h_is_trading_type_real(soup):
            self.username = h_get_username(soup) 
            self.value = h_get_portfolio_value(soup)
            self.total_value = h_get_portfolio_total_value(soup)
            self.stocks = h_get_stocks_list(soup)
        else:
            print('Investing type is Demo, please login in your browser manually and change to Investing first')


def h_get_portfolio_value(soup):
    print('Getting portfolio value...')
    portfolio_value_section = soup.find(class_='portfolio-value')
    portfolio_values = portfolio_value_section.find_all(class_='formatted-price-part')

    portfolio_value_str = ''
    for elem in portfolio_values:
        if elem.string != None:
            portfolio_value_str += elem.string

    return float(remove_currency_signs(portfolio_value_str))

def h_get_portfolio_total_value(soup):
    return float(remove_currency_signs(soup.find(class_='account-status-header-value').string))

def h_get_username(soup):
    print('Getting username')

    return soup.find(class_='username').string
def h_is_trading_type_real(soup):
    return soup.find(class_='trading-type').string.lower() == 'Investing - Real Money'.lower()
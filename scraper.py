import gc
import time

from models.stock import OwnedStock

from msvcrt import getch
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def main():
    with Chrome() as driver:
        open_trading212_page(driver)
        login(driver)
        wait_for_platform_loader(driver)
        click_portfolio_tab(driver)

        total_portfolio_value = get_total_portfolio_value(driver)
        owned_stocks = get_stocks_list(driver)

        total_return = 0
        for stock in owned_stocks:
            print('[{}] {} - {} ({:.2f}%)'.format(stock.stock_type, stock.ticker, stock.total_value, stock.total_value * 100 / total_portfolio_value))
            total_return += stock.return_value
        
        print('Total Portfolio Value: {}'.format(total_portfolio_value))
        print('Return Value: {:.2f} ({:.2f})'.format(total_return, total_return * 100 / (total_portfolio_value - total_return)))

        print('Exiting...')
        time.sleep(3)

def login(driver):
    print('Waiting for login form...')
    email_field = driver.find_element_by_id('username-real')
    password_field = driver.find_element_by_id('pass-real')
    login_button = driver.find_element_by_class_name('button-login')

    print('Source code can be seen at https://github.com/shika-n/trading212-portfolio-scraper')
    print('Do not share credentials with anybody!')

    first_ask = True
    login_button_visible = is_login_button_visible(driver)
    while first_ask or login_button_visible:
        if not first_ask:
            print('Credentials is wrong, please try again\n')

        ask_credentials(email_field, password_field)
        login_button.click()

        first_ask = False

        time.sleep(5)

        login_button_visible = is_login_button_visible(driver)

    print('Login section done.')

def ask_credentials(email_field, password_field):
    email = input('E-mail: ')

    email_field.clear()
    email_field.send_keys(email)
    
    print('Password: ')
    password = ''
    while True:
        ch = getch().decode('utf-8')
        if ch == '\n' or ch == '\r':
            break
        password += ch

    password_field.clear()
    password_field.send_keys(password)
    
    del password
    gc.collect()

    print('Logging in...')

def get_total_portfolio_value(driver):
    print('Getting portfolio value...')
    portfolio_value_section = driver.find_element_by_class_name('portfolio-value')
    portfolio_values = portfolio_value_section.find_elements_by_class_name('formatted-price-part')

    total_portfolio_value_str = ''
    for value in portfolio_values:
        total_portfolio_value_str += value.text

    return float(remove_currency_signs(total_portfolio_value_str))

def get_stocks_list(driver):
    print('Getting investments...')
    investments_section = driver.find_element_by_class_name('investments-section')

    # Faster than getting elements one by one inside a for loop
    stock_tickers = [item.get_attribute('innerHTML') for item in investments_section.find_elements_by_class_name('instrument-logo-name')]
    stock_names = [item.text for item in investments_section.find_elements_by_class_name('text')]
    stock_quantities = [float(item.text.split(' ')[0]) for item in investments_section.find_elements_by_class_name('quantity')]
    stock_total_values = [float(remove_currency_signs(item.text)) for item in investments_section.find_elements_by_class_name('total-value')]
    stock_return_values = [float(remove_currency_signs(item.find_element_by_tag_name('div').text.split(' ')[0])) for item in investments_section.find_elements_by_class_name('return')]
    stock_types = ['Stock' if item.get_attribute('data-qa-item').count('_') == 2 else 'ETF' for item in investments_section.find_elements_by_class_name('investment-item')]
    stock_logo_urls = [item.get_attribute('src') for item in investments_section.find_elements_by_tag_name('img')]

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

def is_login_button_visible(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'button-login')
        return True
    except:
        return False

def click_portfolio_tab(driver):
    print('Clicking on portfolio tab...')
    driver.find_element_by_class_name('portfolio-icon').click()

def wait_for_platform_loader(driver):
    print('Waiting for platform-loader...')
    WebDriverWait(driver, timeout=60).until(EC.invisibility_of_element((By.ID, 'platform-loader')))

def open_trading212_page(driver):
    print('Opening Trading212 website...')
    driver.get('https://www.trading212.com/en/login')

def remove_currency_signs(str):
    return str.replace('$', '').replace(',', '')

if __name__ == '__main__':
    main()
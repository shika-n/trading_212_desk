import gc
from msvcrt import getch # Need for password input, only works in windows

import scraper.scraper as scraper
from models.driver_portfolio import DriverPortfolio
from util.drivers import get_driver

def ask_credentials_terminal():
    email = input('E-mail: ')
    
    print('Password: ')
    password = ''
    while True:
        ch = getch().decode('utf-8')
        if ch == '\n' or ch == '\r':
            break
        password += ch

    return email, password

with get_driver('chrome') as driver:
    # Open page without session token
    if not scraper.open_trading212_page(driver):
        raise 'Failed to open Trading212 page or session token is invalid'

    # Ask credentials and login
    email, password = ask_credentials_terminal()
    if not scraper.login(driver, email, password):
        raise 'Wrong credentials'

    # Not sure if necessary, want it to be short lived
    del password
    gc.collect()

    # Wait until splash screen is gone
    scraper.wait_for_platform_loader(driver)

    # Switch to portfolio section
    scraper.goto_portfolio_section(driver)

    # Initialize portfolio which data is from webdriver
    portfolio = DriverPortfolio(driver)

    for stock in portfolio.stocks:
        print('[{}] {} - {} ({:.2f}%) ({:.2f}%% of total portfolio)'.format(
            stock.stock_type,
            stock.ticker,
            stock.total_value,
            stock.get_return_percentage() * 100,
            portfolio.get_stock_portfolio_percentage(stock) * 100
        ))
    
    print('Total Portfolio Value: {}'.format(portfolio.total_value))
    print('Total Return: {:.2f} ({:.2f}%)'.format(
        portfolio.get_total_return(),
        portfolio.get_total_return_percentage() * 100
    ))

    driver.delete_all_cookies()
    print('Done.')
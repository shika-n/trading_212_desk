import scraper.scraper as scraper

from models.portfolio import Portfolio

from selenium.webdriver import Chrome

with Chrome() as driver:
    scraper.open_trading212_page(driver)
    scraper.login(driver)
    scraper.wait_for_platform_loader(driver)
    scraper.goto_portfolio_section(driver)

    portfolio = Portfolio(driver)

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

    print('Done.')
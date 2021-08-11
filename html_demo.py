from models.html_portfolio import HtmlPortfolio

from bs4 import BeautifulSoup

with open('source.html') as source:
    soup = BeautifulSoup(source, 'html.parser')

    portfolio = HtmlPortfolio(soup)

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
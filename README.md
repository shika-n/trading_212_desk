# trading212-portfolio-scraper
A script to get your portfolio in Trading212 by scraping the web page.

Currently only works on windows' command prompt.

## Requirements
- Python3
- Selenium
- chromedriver

## Usage
- To only view portfolio:
    - Simply run `python demo.py`
- To use the functions:
	- Import the required files:
        - `import import scraper`
        - `from selenium.webdriver import Chrome`
    - Call `open_trading212_page(driver)` to load the page
    - Then, call `login(driver)` which will ask your email and password via stdin
    - Next, call `wait_for_platform_loader(driver)` to wait for the loading screen
    - Call `goto_portfolio_section(driver)` to switch tab to portfolio tab
    - Finally, you can call the functions below:
		- `get_total_portfolio_value(driver)`: get the value on top left of portfolio page (`from models.portfolio import get_total_portfolio_value`)
		- `get_stocks_list(driver)`: get stocks on the investments section just below portfolio chart (`from models.stock import get_stocks_list`)
        - `Portfolio(driver)`: get all data in your portfolio (`from models.portfolio import Portfolio`)
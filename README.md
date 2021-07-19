# trading212-portfolio-scraper
A script to get your portfolio in Trading212 by scraping the web page

## Requirements
- Python3
- Selenium
- chromedriver

## Usage
- To only view portfolio:
    - Simply run `python scraper.py`
- To use the functions:
	- Import the `scraper.py` file
    - Call `open_trading212_page(driver)` to load the page
    - Then, call `login(driver)` which will ask your email and password via stdin
    - Next, call `wait_for_platform_loader(driver)` to wait for the loading screen
    - Call `click_portfolio_tab(driver)` to switch tab to portfolio tab
    - Finally, you can call the functions below:
		- `get_total_portfolio_value(driver)`: get the value on top left of portfolio page
		- `get_stocks_list(driver)`: get stocks on the investments section just below portfolio chart
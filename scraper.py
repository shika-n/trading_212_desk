import gc
import time

from msvcrt import getch
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

def is_login_button_visible(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'button-login')
        return True
    except:
        return False

def goto_portfolio_section(driver):
    print('Clicking on portfolio tab...')
    driver.find_element_by_class_name('portfolio-icon').click()
    driver.find_element_by_class_name('investment-tab').click()

def wait_for_platform_loader(driver):
    print('Waiting for platform-loader...')
    WebDriverWait(driver, timeout=60).until(EC.invisibility_of_element((By.ID, 'platform-loader')))

def open_trading212_page(driver):
    print('Opening Trading212 website...')
    driver.get('https://www.trading212.com/en/login')
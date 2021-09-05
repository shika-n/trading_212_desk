import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(driver, email, password):
    print('Waiting for login form...')
    email_field = driver.find_element_by_name('email')
    password_field = driver.find_element_by_name('password')
    login_button = driver.find_element_by_class_name('submit-button_input__3s_QD')

    print('Source code can be seen at https://github.com/shika-n/trading212-portfolio-scraper')
    print('Do not share credentials with anybody!')

    # Input email
    email_field.clear()
    email_field.send_keys(email)

    # Input password
    password_field.clear()
    password_field.send_keys(password)

    # Click on login button
    login_button.click()

    # Give time to login and screen transition
    time.sleep(5)

    # Check if login button is still visible (failed to login)
    login_button_visible = is_login_button_visible(driver)
    if login_button_visible:
        return False

    return True

def goto_portfolio_section(driver):
    print('Clicking on portfolio tab...')
    driver.find_element_by_class_name('portfolio-icon').click()
    WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'investment-tab')))
    driver.find_element_by_class_name('investment-tab').click()

def wait_for_platform_loader(driver):
    print('Waiting for platform-loader...')
    WebDriverWait(driver, timeout=60).until(EC.invisibility_of_element((By.ID, 'platform-loader')))

def open_trading212_page(driver, session_token=None, expiry=None):
    print('Opening Trading212 login page...')
    driver.get('https://www.trading212.com/en/login')

    if session_token != None:
        print('Opening Trading212 with provided session token...')

        session_cookie = {
            'name': 'TRADING212_SESSION_LIVE',
            'value': session_token,
            'domain': '.trading212.com',
            'path': '/',
            'secure': True,
            'httpOnly': True
        }

        if expiry != None:
            session_cookie['expiry'] = expiry

        driver.add_cookie(session_cookie)
        
        driver.get('https://live.trading212.com/')

        # Give time for screen transition
        time.sleep(5)

        return is_platform_loader_visible(driver)
    
    return True

def is_login_button_visible(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'submit-button_input__3s_QD')
        return True
    except:
        return False

def is_platform_loader_visible(driver):
    try:
        driver.find_element(By.ID, 'platform-loader')
        return True
    except:
        return False

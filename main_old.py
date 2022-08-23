import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_driver() -> webdriver:
    dr: webdriver = webdriver.Chrome('source/chromedriver.exe')
    dr.maximize_window()
    return dr

def close_driver(dr: webdriver):
    dr.close()
    dr.quit()

def login_check(dr: webdriver, name: str, pas: str) -> webdriver:
    dr.find_element(By.ID, 'user-name').send_keys(name)
    dr.find_element(By.NAME, 'password').send_keys(pas)
    dr.find_element(By.ID, 'login-button').click()
    return dr

if __name__ == '__main__':
    driver = setup_driver()
    driver.get('https://www.saucedemo.com/')
    driver = login_check(driver, 'standard_user', 'secret_sauce')
    time.sleep(3)




    print('PyCharm')
   # close_driver(driver)


from time import sleep
from selenium import webdriver


def get_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://dubai.dubizzle.com/")

    login_button = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div/div[2]/button[3]')
    login_button.click()

    login_by_email = driver.find_element_by_xpath('//*[@id="popup_login_link"]')
    login_by_email.click()

    username = driver.find_element_by_xpath('//*[@id="popup_email"]')
    username.clear()
    username.send_keys('sample@gmail.com')

    password = driver.find_element_by_xpath('//*[@id="popup_password"]')
    password.clear()
    password.send_keys('sample password')

    login_btn = driver.find_element_by_xpath('//*[@id="popup_login_btn"]')
    login_btn.click()

    cookie = driver.get_cookie()
    return cookie

    driver.close()




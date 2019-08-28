from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd


#there might be a one-liner here that can grab the maybe even with selenium-requests 
#https://github.com/cryzed/Selenium-Requests

def login(driver) -> None:

    email = 'email@gmail.com'
    pw = 'temppass'

    driver.get('https://vimeo.com/log_in')
    driver.find_element_by_id('signup_email').send_keys(email)
    driver.find_element_by_id('login_password').send_keys(pw)

    driver.find_element_by_class_name('js-email-submit').click()

def navigate(driver) -> List:

    url = 'https://vimeo.com/stats/source'
    driver.get(url)
    driver.find_element_by_xpath("//button[@data-filter='filmfreeway.com']").click()
    return [x.text for x in driver.find_elements_by_class_name('level1')]

def main():
    driver = webdriver.Firefox()
    login(driver)
    print(navigate(driver))

if __name__ == '__main__':
    main()

from asyncore import loop
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest


def test_qr():
    global driver
    # Run Test With One Participant [Partial Paid with Tip]
    driver = webdriver.Chrome()
    # Add restaurant link
    location = ('https://app-staging.qlub.cloud/qr/ae/dummyStripeSezai/55/_/_/b3b23292cd')
    driver.get(location)
    sleep(10)

    # fetchOrder
    driver.find_element(By.XPATH, '//span[@class="wrapper"]/span').click()
    sleep(10)

    #Click Refresh
    driver.refresh()
    sleep(15)

    # Enter Card Number
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH, '//*[@id="Field-numberInput"]').send_keys("4242424242424242")
    driver.switch_to.default_content()
    # Enter Expiry Date
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH, '//*[@id="Field-expiryInput"]').send_keys("1030")
    driver.switch_to.default_content()
    # Enter CVC
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH, '//*[@id="Field-cvcInput"]').send_keys("100")
    driver.switch_to.default_content()
    sleep(5)

    # Click On Pay Now
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[2]').click()
    sleep(35)

    driver.quit()
    print('Successfull Payment')
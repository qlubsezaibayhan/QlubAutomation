from asyncore import loop
#from http.client import ACCEPTED
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
def test_qr():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    location = ('https://app-staging.qlub.cloud/qr/ae/dummyStripeSezai/17/_/_/83f58ea03f')
    driver.get(location)
    sleep(10)

    # fetchOrder
    driver.find_element(By.XPATH, '//span[@class="wrapper"]/span').click()
    sleep(10)

    # Enter Card Number
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH,'//*[@id="Field-numberInput"]').send_keys("4000002500003155")
    driver.switch_to.default_content()
    # Enter Expiry Date
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH,'//*[@id="Field-expiryInput"]').send_keys("0930")
    driver.switch_to.default_content()
    # Enter CVC
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[1]/div/div/div/div/div[2]/form/div[1]/div[1]/div/iframe'))
    driver.find_element(By.XPATH,'//*[@id="Field-cvcInput"]').send_keys("100")
    driver.switch_to.default_content()
    sleep(5)

    # Click On Pay Now
    driver.find_element(By.XPATH, '//span[normalize-space()="Pay Now"]').click()
    sleep(15)

    driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/div/iframe'))
    driver.find_element(By.XPATH,'//button[@id="test-source-authorize-3ds"]').click()
    driver.switch_to.default_content()
    sleep(20)

    driver.quit()
    print('Successfull Payment')
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
    location = ('https://app-staging.qlub.cloud/qr/ae/SezaiMAFDiscount/9/_/_/d6e213021d')
    driver.get(location)
    sleep(10)

    #fetchOrder
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div/div[2]/main/div/div/div[3]/button[1]').click()
    sleep(10)


    #SplitBill
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[2]/div/div[2]/div[2]/button[1]').click()
    sleep(3)

    driver.find_element(By.XPATH,'//*[@id="select-custom"]').click()
    sleep(3)

    driver.find_element(By.XPATH,'//*[@id="fullWidth"]').send_keys('5')
    sleep(3)
    driver.find_element(By.ID,'split-bill').click()
    sleep(2)

    # AddTip
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[1]/div[2]/div/div[1]/div').click()
    sleep(2)



    #OpencardOption
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[2]').click()
    sleep(3)

    # Enter Card Number
    driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys("4456530000001005")
    sleep(2)
    # Enter Expiry Date
    driver.find_element(By.ID,'cardExpiry').send_keys("1033")
    sleep(2)
    # Enter CVC
    driver.find_element(By.NAME,'securityCode').send_keys("101")
    sleep(2)

    # Click On Pay Now
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[2]/main/div/div/div[5]/div/div/div[4]/div[5]/div/button').click()
    sleep(35)
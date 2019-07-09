# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
 

GOOGLE_CHROME_BIN = os.environ['GOOGLE_CHROME_BIN']
CHROME_DRIVER = os.environ['CHROME_DRIVER']

def _get_options():
    options = Options()
    options.add_argument("--headless")
    # options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options



driver = webdriver.Chrome(executable_path=CHROME_DRIVER,options=_get_options())
driver.get("https://kinposter3.000webhostapp.com/login")
time.sleep(2)

usuario = driver.find_element_by_xpath('//*[@id="username"]')
usuario.send_keys('guille16')
time.sleep(2)
contrasena = driver.find_element_by_xpath('//*[@id="password"]')
contrasena.send_keys('emanuel19')

driver.find_element_by_xpath('//*[@id="signinBtn"]').click()

driver.find_element_by_xpath('/html/body/div[2]/aside/section/ul/li[5]/a/span[1]').click()

time.sleep(1)

driver.find_element_by_xpath('/html/body/div[2]/aside/section/ul/li[5]/ul/li[1]/a/span').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="3"]/span/i').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="groupsDataTable"]/thead/tr[3]/th[1]/label').click()

time.sleep(2)

element = driver.find_element_by_name('post')
driver.execute_script("arguments[0].click();", element)

time.sleep(3600)

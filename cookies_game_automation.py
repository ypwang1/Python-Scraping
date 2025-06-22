from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
time.sleep(5)

consent = driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p')
consent.click()

time.sleep(3)

language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language.click()

time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")

wait_time = 5
timeout = time.time() + wait_time
five_min = time.time() + 60 * 5
while True:
    cookie.click()

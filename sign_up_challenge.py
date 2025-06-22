from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get(url=URL)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Yupeng")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Wang")
email = driver.find_element(By.NAME, value="email")
email.send_keys("ericwyp92@fgmail.com")
button = driver.find_element(By.CSS_SELECTOR, value="button")
button.send_keys(Keys.ENTER)
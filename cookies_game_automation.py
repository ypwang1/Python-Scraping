from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://ozh.github.io/cookieclicker/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
time.sleep(5)


language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language.click()

time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")

wait_time = 5
timeout = time.time() + wait_time
five_min = time.time() + 60 * 5
while True:
    cookie.click()
    if time.time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies").text
            cookies_text = cookies_element.split(" ")[0]
            cookies_amount = int(cookies_text)

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        timeout = time.time() + wait_time
    if time.time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break
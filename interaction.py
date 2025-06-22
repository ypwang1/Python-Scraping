from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
count.click()
print(count.text)


# Fine element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="....")
all_portals.click()

#Find the "Search" <input> by Name

search = driver.find_element(By.NAME, value="search")

# Input the value and enter
search.send_keys("Python", Keys.ENTER)


driver.quit()
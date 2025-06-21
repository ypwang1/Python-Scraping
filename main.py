from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = "https://www.python.org/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

content = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.split("\n")
print(content)
date = []
title = []
for i in range(0, len(content), 2):
    date.append(content[i])
    title.append(content[i+1])

events = {}
for i in range (0, len(date)):
    events[i] = {
        "time": date[i],
        "name": title[i]
    }

print(events)


# text_0 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a').text


# path = driver.find_element(By.XPATH ,'//*[@id="CardInstanceJU1erWIIm_fJ1o3HDfACIg"]/div[1]/a')



# Just close the tap
# driver.close()
# Shunt down the entire browser
driver.quit()
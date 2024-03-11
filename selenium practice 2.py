from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import csv
import pandas as pd

# def product_name(product_name_list,price_name_list):
#     Gin_product_name = driver.find_elements(By.XPATH, "//h3[contains(@class,'name')]")
#
#     for i in Gin_product_name:
#         product_name_list.append(i.text)
#     print(product_name_list)
#     print(len(product_name_list))
#     price_page = driver.find_elements(By.XPATH, "//div[@class='prc']")
#     for price in price_page:
#         # print(price.text)
#         price_name_list.append(price.text)
#     print(price_name_list)
#     print(len(price_name_list))
# def scroll():
#     driver.execute_script("window.scrollTo(0, 2000);")
#     time.sleep(2)

driver = webdriver.Chrome()
driver.get("https://www.jumia.co.ke/spirits-liquors/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
actions = ActionChains(driver)

login_page =driver.find_element(By.XPATH,'//*[@id="pop"]/div/section/button')
login_page.click()
time.sleep(2)

cookies =driver.find_element(By.XPATH,"//button[@aria-label='Close banner']")
cookies.click()
time.sleep(2)
product_name_list = []
price_name_list= []
gin =driver.find_element(By.XPATH,'//*[@id="ctlg"]/div/div[1]/section/div/div/div[4]/a/div/img')
gin.click()
time.sleep(2)

for i in range(2):
    product_name(product_name_list,price_name_list)
    scroll()

gin_nextpage =driver.find_element(By.XPATH,"//a[contains(@class,'pg _act')]")
gin_nextpage.click()
time.sleep(2)
for i in range(2):
    product_name(product_name_list,price_name_list)
    scroll()

gin_nextpage1 =driver.find_element(By.XPATH,"//a[contains(@class,'pg')][6]")
gin_nextpage1.click()
time.sleep(2)
for i in range(2):
    product_name(product_name_list,price_name_list)
    scroll()


final1 = {'PRODUCT NAME': product_name_list}
df = pd.DataFrame(final1)
df.to_csv('final1.csv')

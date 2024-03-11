from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import csv
import pandas as pd


drive = webdriver.Chrome()
drive.get("https://www.schiphol.nl/en/at-schiphol/shop/")
time.sleep(2)
drive.maximize_window()
time.sleep(2)
drive.execute_script("window.scrollTo(0, 1000);")
time.sleep(2)
aero_button=drive.find_element(By.XPATH,"/html/body/header/div[2]/div[2]/div/div/div[2]/div/button")
aero_button.click()
time.sleep(2)
aero_button.click()
time.sleep(2)
food_and_drink=drive.find_element(By.XPATH,"/html/body/header/div[2]/div[2]/div/div/div[2]/div/ul/li[6]/a/div[2]/span")
food_and_drink.click()
time.sleep(2)
accept_cookies = drive.find_element(By.XPATH, "//span[contains(text(),'Yes, I accept all cookies')]")
accept_cookies.click()
time.sleep(2)
drinks = drive.find_element(By.XPATH, "//button[text()='Drinks']")
time.sleep(2)
drinks.click()
time.sleep(2)

Product_name = drive.find_elements(By.XPATH, "//span[contains(@class,'R6Z9B _4YY8f MUapD yY7uJ _8VJGH YVomU')]")
product_name_list = []
for i in Product_name:
    product_name_list.append(i.text)

discount = []
price_name = drive.find_elements(By.XPATH, "//div[contains(@class,'-OX0o')]")
product_price_list = []
for j in price_name:
    content = j.text
    a = 'from'
    if a in content:
        before_current, after_current = content.split("Current", 1)
        discount.append(before_current.strip())
        product_price_list.append("Current" + after_current)
    else:
        product_price_list.append(content)
        discount.append("NIL")

drive.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
drive.execute_script("window.scrollBy(0,1000)", "")
time.sleep(1)
drive.execute_script("window.scrollBy(0,1000)", "")
time.sleep(1)
drinks_page_two = drive.find_element(By.XPATH, "//button[contains(@class, 'BaRFD') and text()='2']")
drinks_page_two.click()
time.sleep(2)

product_name_2 = drive.find_elements(By.XPATH, "//span[contains(@class, 'R6Z9B _4YY8f MUapD yY7uJ _8VJGH YVomU')]")
for k in product_name_2:
    product_name_list.append(k.text)

product_price_2 = drive.find_elements(By.XPATH, "//div[contains(@class, '-OX0o')]")
for s in product_price_2:
    content = s.text
    a = 'from'
    if a in content:
        before_current, after_current = content.split("Current", 1)
        discount.append(before_current.strip())
        product_price_list.append("Current" + after_current)
    else:
        product_price_list.append(content)
        discount.append("NIL")

print(product_price_list)
print(product_name_list)
print(discount)

final = {'PRODUCT NAME': product_name_list, 'PRICE': product_price_list, 'DISCOUNT': discount}
df = pd.DataFrame(final)
df.to_csv('final.csv')
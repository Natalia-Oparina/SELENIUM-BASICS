from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

url='http://automationpractice.com/index.php?controller=contact'

driver.get(url)

element=driver.find_element(By.CSS_SELECTOR,"p")
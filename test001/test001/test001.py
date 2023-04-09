from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

Name = "C111151112"
Pass = "Aa0909262309"

driver = webdriver.Chrome('./chromedriver')
driver.get('https://elearning.nkust.edu.tw/mooc/login.php')
actions = ActionChains(driver)

a = driver.find_element(By.ID, 'username')            
b = driver.find_element(By.ID, 'password')  
c = driver.find_element(By.ID, 'btnSignIn')  

actions.click(a).send_keys(Name)
actions.perform()
actions.click(b).send_keys(Pass)
actions.perform()  
c.click()  

time.sleep(5)
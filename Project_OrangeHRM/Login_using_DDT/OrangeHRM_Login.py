from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtil

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

file = r"D:\Project(OrangeHRM)\Project_OrangeHRM\Login_using_DDT\DateDriven.xlsx"

rows = XLUtil.getRowCount(file,'Sheet1')

for r in range(2,rows+1):
    username = XLUtil.readData(file,'Sheet1',r,7)
    password = XLUtil.readData(file, 'Sheet1', r, 8)

    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(password)

    login_btn = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

   # if

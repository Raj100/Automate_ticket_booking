import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui

os.environ['PATH'] += r"/Users/raj/Documents/Python/chromedriver_mac64"
driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(2)
raj=driver.find_element(By.CLASS_NAME, "ng-tns-c57-8")
raj.click()
pyautogui.typewrite("MADGAON - MAO (MADGAON)\n")
time.sleep(10)
driver.quit()

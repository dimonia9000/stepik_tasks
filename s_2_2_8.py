from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from time import sleep
from os import path

url = "http://suninjuly.github.io/file_input.html"

try:
	browser = WD.Chrome()
	browser.get(url)
	browser.find_element(By.NAME, "firstname").send_keys("Ivan")
	browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
	browser.find_element(By.NAME, "email").send_keys("tes@tws.wq")
	browser.find_element(By.NAME, "file").send_keys(path.abspath("new.txt"))
	browser.find_element(By.CLASS_NAME, "btn").click()

finally:
	sleep(15)
	browser.quit()

from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

ceil = lambda x: str(log(abs(12 * sin(x))))
url = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = WD.Chrome()
	browser.get(url); sleep(1)
	browser.find_element(By.TAG_NAME, "button").click(); sleep(1)
	browser.switch_to.alert.accept()
	x = int(browser.find_element(By.ID, "input_value").text)
	browser.find_element(By.ID, "answer").send_keys(ceil(x))
	browser.find_element(By.TAG_NAME, "button").click()

finally:
	sleep(10)
	browser.quit()

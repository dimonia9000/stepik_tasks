from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

func = lambda x: str(log(abs(12 * sin(x))))

try:
	browser = WD.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	WDW(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	browser.find_element(By.ID, "book").click()
	x = int(browser.find_element(By.ID, "input_value").text)
	browser.find_element(By.ID, "answer").send_keys(func(x))
	browser.find_element(By.ID, "solve").click()
	print(browser.switch_to.alert.text)

finally:
	browser.quit()
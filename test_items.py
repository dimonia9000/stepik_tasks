from selenium.webdriver.common.by import By
from time import sleep

def test_find_add_to_basket_btn(browser):
	browser.get("https://selenium1py.pythonanywhere.com/catalogue/the-hacker-crackdown_183")
	sleep (15)

	try:
		button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

	except:
		button = False

	assert button, "element Add to basket(.btn-primary) fon found"

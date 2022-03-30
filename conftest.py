import pytest
from selenium import webdriver as WD
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption("--browser_name", action="store", default="chrome",
		help="Choose: chrome or firefox", choices=("chrome", "firefox"))
	parser.addoption("--language", action="store", default="ru",
		help="Choose language")

@pytest.fixture(scope="session")
def browser(request):
	browser_name = request.config.getoption("--browser_name")
	user_lang = request.config.getoption("--language")
	browser = None
	
	if browser_name == "chrome":
		print("\nstart chrome browser for test..")
		options = Options()
		options.add_experimental_option("prefs", {"intl.accept_languages": user_lang})
		browser = WD.Chrome(options=options)
	
	elif browser_name == "firefox":
		print("\nstart firefox browser for test..")
		fp = WD.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_lang)
		browser = WD.Firefox(firefox_profile=fp)
	yield browser
	print("\nquit browser..")
	browser.quit()

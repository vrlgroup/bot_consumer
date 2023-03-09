from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def getDriver(path: str = "/usr/bin/chromedriver"):
    service = ChromeService(executable_path=ChromeDriverManager().install())

    return webdriver.Chrome(service=service)

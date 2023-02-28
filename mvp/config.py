from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def getDriver(path: str = "/usr/bin/chromedriver"):
    service = Service(executable_path=path)
    return webdriver.Chrome(service=service)

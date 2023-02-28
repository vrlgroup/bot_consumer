from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def messageContainsEmoji(msg: str):
    contains = False

    for char in msg:
        if char == ":":
            contains = True

    return contains

def findAndSelectElement(driver: webdriver, xpath: str):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

def openWebsite(driver: webdriver, url: str):
    return driver.get(url)
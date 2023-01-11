from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.sheet import *
from utils.convert import *
from utils.web import *
from common.wait import *
from env.widgets import *

def configureDriver(path:str):
    return Service(executable_path=path)

def openBrowser(driver : webdriver, url : str):
    driver.get(url)
    return

def sendMessage(driver:webdriver, msg):
    input = driver.find_element(By.XPATH, chatInputXpath)
    input.send_keys(msg)

    submitButton = driver.find_element(By.XPATH, chatSubmitMessageBtnXpath)
    submitButton.click()

def findAndOpenConversation(driver:webdriver, name:str):
    searchbar = driver.find_element(By.XPATH, searchbarXpath)
    searchbar.click()

    searchbarInput = driver.find_element(By.XPATH, searchbarInputXpath)
    searchbarInput.send_keys(name)
    
    wait(5, "Waiting results")

    searchbarInput.send_keys(Keys.ARROW_DOWN)
    searchbarInput.send_keys(Keys.RETURN)

    return
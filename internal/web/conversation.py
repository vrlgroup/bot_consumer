from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from web.utils import findAndSelectElement
from common.wait import wait
from widgets import *

def openPrivateConversation(driver: webdriver):
    privateGroupName = "Teste bot"
    findAndOpenConversation(driver, privateGroupName)


def findAndOpenConversation(driver: webdriver, name: str):
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).click()
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(name)

    wait(5, "Waiting results")

    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.ARROW_DOWN)
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.RETURN)

    return

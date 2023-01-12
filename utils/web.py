from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.convert import *
from utils.web import *
from common.wait import *
from env.widgets import *
from common.variables import driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def configureDriver(path: str):
    return Service(executable_path=path)


def openBrowser(driver: webdriver, url: str):
    driver.get(url)
    return

def selectElement(driver: webdriver, xpath: str):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))


def messageContainsEmoji(msg: str):
    contains = False

    for char in msg:
        if char == ":":
            contains = True

    return contains


def sendMessage(driver: webdriver, msg: str):
    selectElement(driver, CHAT_INPUT_XPATH).send_keys(msg)

    if messageContainsEmoji(msg):
        selectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)

    selectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)


def findAndOpenConversation(driver: webdriver, name: str):
    selectElement(driver, SEARCHBAR_INPUT_XPATH).click()
    selectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(name)

    wait(5, "Waiting results")

    selectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.ARROW_DOWN)
    selectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.RETURN)

    return


def openPrivateGroup(driver: webdriver):
    privateGroupName = "Teste bot"
    findAndOpenConversation(driver, privateGroupName)


def selectLatestMessages(driver: webdriver):
    lastId = 1
    _xpath = f"{FORWARD_GROUP_MESSAGE_DIV}/div[{lastId}]"

    try:
        selectElement(driver, _xpath)
        lastId+=1
    except:
        print(f"LastId {lastId}")

    selectElement(driver, _xpath).click()
    wait(2, "Nothing")
    
    return


def openForwardMessageModal(driver: webdriver):
    selectElement(driver, GROUP_SETTINGS_XPATH).click()
    selectElement(driver, SELECT_GROUP_MESSAGES_XPATH).click()

    return

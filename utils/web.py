from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.convert import *
from utils.web import *
from common.wait import *
from env.widgets import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def configureDriver(path: str):
    return Service(executable_path=path)


def openBrowser(driver: webdriver, url: str):
    driver.get(url)
    return

def findAndSelectElement(driver: webdriver, xpath: str):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))


def messageContainsEmoji(msg: str):
    contains = False

    for char in msg:
        if char == ":":
            contains = True

    return contains


def sendMessage(driver: webdriver, msg: str):
    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(msg)

    if messageContainsEmoji(msg):
        findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)

    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)


def findAndOpenConversation(driver: webdriver, name: str):
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).click()
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(name)

    wait(5, "Waiting results")

    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.ARROW_DOWN)
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.RETURN)

    return


def openPrivateGroup(driver: webdriver):
    privateGroupName = "Teste bot"
    findAndOpenConversation(driver, privateGroupName)


def selectFirstMessages(driver: webdriver):
    findAndSelectElement(driver, SELECT_GROUP_MESSAGES_XPATH)

    # wait(30, "Waiting to sync messages")

    path = "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[2]"
    msgs = driver.find_elements(By.XPATH, path)
    for message in msgs:
        message.click()

    path = "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[3]"
    msgs = driver.find_elements(By.XPATH, path)
    for message in msgs:
        message.click()

    findAndSelectElement(driver, "/html/body/div[1]/div/div/div[4]/div/span[2]/div/button[4]/span").click()

    return


def openForwardMessageModal(driver: webdriver):
    findAndSelectElement(driver, GROUP_SETTINGS_XPATH).click()
    findAndSelectElement(driver, SELECT_GROUP_MESSAGES_XPATH).click()

    return

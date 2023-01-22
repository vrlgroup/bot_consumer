from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.wait import wait
from .utils import findAndSelectElement
from .utils import messageContainsEmoji
from .widgets import *

def sendMessage(driver: webdriver, msg: str):
    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(msg)

    if messageContainsEmoji(msg):
        findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)

    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)


def selectMessagesToForward(driver: webdriver):
    findAndSelectElement(driver, SELECT_GROUP_MESSAGES_XPATH)

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
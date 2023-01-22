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


def findAndSelectMessageById(driver: webdriver, i: int):
    path = f"{GROUP_MESSAGES_LIST_BASE_XPATH}/div[{i}]"
    msgs = driver.find_elements(By.XPATH, path)
    for message in msgs:
        message.click()

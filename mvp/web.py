from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.widgets import *
from common.wait import wait


def openWebsite(driver: webdriver, url: str):
    return driver.get(url)


def findAndSelectElement(driver: webdriver, xpath: str):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))


def openPrivateConversation(driver: webdriver):
    privateGroupName = "Teste bot"
    findAndOpenConversation(driver, privateGroupName)


def findAndOpenConversation(driver: webdriver, name: str):
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).click()
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).clear()
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(name)

    wait(2, "Waiting results")

    findAndSelectElement(
        driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.ARROW_DOWN)
    findAndSelectElement(driver, SEARCHBAR_INPUT_XPATH).send_keys(Keys.RETURN)

    return


def enableSelectGroupMessages(driver: webdriver):
    findAndSelectElement(
        driver, "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div").click()
    findAndSelectElement(
        driver, "/html/body/div[1]/div/span[4]/div/ul/div/div/li[2]").click()


def sendMessage(driver: webdriver, msg: str):
    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(msg)
    findAndSelectElement(driver, CHAT_INPUT_XPATH).send_keys(Keys.RETURN)


def findAndSelectMessageById(driver: webdriver, i: int):
    path = f"{GROUP_MESSAGES_LIST_BASE_XPATH}/div[{i}]"
    msgs = driver.find_elements(By.XPATH, path)
    for message in msgs:
        message.click()


def selectMessagesToForward(driver: webdriver):
    findAndSelectMessageById(driver, 5)


def selectGroupsToForward(driver: webdriver, groupsSuffixes: list[str]):
    # findAndSelectElement(driver, FORWARDMODAL_SEARCHBAR_INPUT_XPATH).click()

    # for suffix in groupsSuffixes:
    #     findAndSelectElement(
    #         driver, FORWARDMODAL_SEARCHBAR_INPUT_XPATH).send_keys(suffix)

    #     wait(1, "Waiting for result")

    #     findAndSelectElement(
    #         driver, FORWARDMODAL_FIRST_RESULT_AFTER_SEARCH_XPATH).click()
    return


def whatsAppAuthentication(driver):
    openWebsite(driver, "https://web.whatsapp.com")

    didScanQrCode = False
    while didScanQrCode == False:
        try:
            driver.find_element(By.XPATH, SEARCHBAR_INPUT_XPATH)
            didScanQrCode = True
        except:
            wait(5, f"Authentication failed! Trying again soon")

from utils.sheet import *
from utils.convert import *
from utils.web import *
from common.wait import *
from env.widgets import *

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
from random import randint

def main():
    getCsvGroups()

    service = configureDriver("C:/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    openBrowser(driver, "https://web.whatsapp.com")
    wait(30, "Waiting to read Qr code")

    # 1) Send message to private group
    privateGroupName = "Teste bot"
    findAndOpenConversation(driver, privateGroupName)
    sendMessage(driver, "Mensagem teste")

    # 2) Forward messages
    groupSettings = driver.find_element(By.XPATH, groupSettingsXpath)
    groupSettings.click()

    selectMessagesButton = driver.find_element(By.XPATH, groupSelectMessagesXpath)
    selectMessagesButton.click()

    messagesList = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]")
    messagesListChildren = messagesList.find_elements(By.XPATH, ".//*")
    messagesListChildrenCount = len(messagesListChildren)
    messagesToForward = []

    if messagesListChildrenCount < 2:
        print(f"Error, we found only {messagesListChildrenCount} but must be at least 2")
        return

    for k, message in enumerate(messagesListChildren):
        if k == messagesListChildrenCount or k == messagesListChildrenCount - 1:
            # messagesToForward.append(message)
            message.click()

    for row in messagesToForward:
        # .row > div > div > div > div > div > div > div > div > span
        print(row)

    # # Quebrou aqui
    # firstMessageCheckbox = driver.find_element(By.XPATH, firstMessageCheckboxXpath)
    # firstMessageCheckbox.click()

    # forwardMessageSpan = driver.find_element(By.XPATH, forwardMessageSpanXpath)
    # forwardMessageSpan.click()

    # selectGroup = driver.find_element(By.XPATH, forwardSelectFirstGroupXpath)
    # selectGroup.click()

    # submitButton = driver.find_element(By.XPATH, forwardMessageSubmitXpath)
    # submitButton.click()

    wait(20, "Finishing process")


main()
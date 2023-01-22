from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.wait import wait
from internal.web.utils import openWebsite
from internal.web.conversation import openPrivateConversation, openForwardMessageModal
from internal.web.messages import sendMessage, selectMessagesToForward
from internal.web.widgets import *
from internal.web.config import *

from internal.sheet.get import buildCsvToGroups


def main():
    groups = buildCsvToGroups()

    service = configureDriver("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    openWebsite(driver, "https://web.whatsapp.com")

    didScanQrCode = False
    while didScanQrCode == False:
        try:
            driver.find_element(By.XPATH, SEARCHBAR_INPUT_XPATH)
            didScanQrCode = True
        except:
            wait(5, "User didn't scan qr code")
            didScanQrCode = False

    openPrivateConversation(driver)
    sendMessage(driver, "Mensagem teste :rockets")
    sendMessage(driver, "Mensagem teste")

    openForwardMessageModal(driver)
    selectMessagesToForward(driver)

    wait(20, "Finishing process")


main()

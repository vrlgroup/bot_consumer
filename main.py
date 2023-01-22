from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.wait import *
from internal.web.utils import *
from internal.web.conversation import *
from internal.web.messages import *
from internal.web.widgets import *
from internal.web.config import *
from internal.web.forward import *


from internal.sheet.get import *


def main():
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
    # sendMessage(driver, "Mensagem teste :rockets")
    # sendMessage(driver, "Mensagem teste")

    enableSelectGroupMessages(driver)
    wait(2, "waiting...")
    
    selectMessagesToForward(driver)
    findAndSelectElement(driver, FORWARD_MESSAGE_BUTTON_DURING_SELECT_MESSAGES).click()

    groups = readCSVWithSuffix('001')
    selectGroupsToForward(driver, groups)
    findAndSelectElement(driver, FORWARDMODAL_SUBMIT_GROUPS_SELECTED).click()

    wait(20, "Finishing process")


main()
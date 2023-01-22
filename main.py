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

import math


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

    mustContinue = True
    while mustContinue:
        # openPrivateConversation(driver)
        # sendMessage(driver, "Mensagem teste :rockets")
        # sendMessage(driver, "Mensagem teste")

        groups = readCSVWithSuffix('001')
        sliceSize = 2  # Mudar para 5
        slicesToCut = math.ceil(len(groups)/sliceSize)
        slices = []
        for i in range(slicesToCut):
            startSliceAt = sliceSize * i
            endSliceAt = startSliceAt + sliceSize
            slices.append(groups[startSliceAt:endSliceAt])

        for groupSlices in slices:
            openPrivateConversation(driver)
            wait(5, "waiting...")

            enableSelectGroupMessages(driver)
            wait(5, "waiting...")

            selectMessagesToForward(driver)
            findAndSelectElement(
                driver, FORWARD_MESSAGE_BUTTON_DURING_SELECT_MESSAGES_XPATH).click()

            selectGroupsToForward(driver, groupSlices)
            findAndSelectElement(
                driver, FORWARDMODAL_SUBMIT_GROUPS_SELECTED_XPATH).click()

        # BUG - Se for numero impar ta quebrando

        openPrivateConversation(driver)
        wait(1, "waiting...")
        enableSelectGroupMessages(driver)
        wait(1, "waiting...")
        findAndSelectElement(
            driver, DELETE_MESSAGE_BUTTON_DURING_SELECT_MESSAGE_XPATH).click()
        wait(1, "waiting...")
        findAndSelectElement(driver, DELETE_ONLY_FOR_ME_BUTTON_XPATH).click()

        # Tentar buscar pelo id 5 e 6 novamente, se parar execucao, ok
        mustContinue = False

    wait(20, "Finishing process")


main()

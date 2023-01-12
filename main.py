from utils.sheet import *
from utils.convert import *
from utils.web import *
from common.wait import *
from common.variables import *
from env.widgets import *

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from random import randint

def main():
    getCsvGroups()

    service = configureDriver("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    openBrowser(driver, "https://web.whatsapp.com") 

    didScanQrCode = False
    while didScanQrCode == False:
        try:
            driver.find_element(By.XPATH, SEARCHBAR_INPUT_XPATH)
            didScanQrCode = True
        except:
            wait(5, "User didn't scan qr code")
            didScanQrCode = False


    openPrivateGroup(driver)
    sendMessage(driver, "Mensagem teste :rockets")
    sendMessage(driver, "Mensagem teste")

    openForwardMessageModal(driver)
    selectLatestMessages(driver)

    wait(20, "Finishing process")


main()
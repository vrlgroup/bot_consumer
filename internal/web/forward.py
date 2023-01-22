# findAndSelectElement(driver, FORWARDMODAL_SEARCHBAR_INPUT_XPATH).send_keys()
from selenium import webdriver
from .messages import findAndSelectMessageById
from .utils import *
from .widgets import *
from common.wait import *

from internal.models.group import *


def selectMessagesToForward(driver: webdriver):
    findAndSelectMessageById(driver, 5)
    findAndSelectMessageById(driver, 6)

def selectGroupsToForward(driver: webdriver, groupsSuffixes: list[str]):
    findAndSelectElement(driver, FORWARDMODAL_SEARCHBAR_INPUT_XPATH).click()

    for suffix in groupsSuffixes:
        findAndSelectElement(
            driver, FORWARDMODAL_SEARCHBAR_INPUT_XPATH).send_keys(suffix)
        wait(1, "Waiting for result")

        findAndSelectElement(
            driver, FORWARDMODAL_FIRST_RESULT_AFTER_SEARCH_XPATH).click()
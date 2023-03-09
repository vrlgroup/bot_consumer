from common.widgets import *
from common.groups import PRIVATE_GROUPS_BY_PRESET
from web import *
from config import getDriver
from selenium import webdriver
from groups_utils import getGroupsSlices

def main():
    _msg = """
Which preset you want use?
1) VRL_01 - VRL_50
> """

    PRESET_ID = int(input(_msg))
    PRESET_ID -= 1

    privateGroupName: str = PRIVATE_GROUPS_BY_PRESET[PRESET_ID]
    slices: list[list[str]] = getGroupsSlices(PRESET_ID)
    
    driver: webdriver = getDriver()

    whatsAppAuthentication(driver=driver)
    print("Auth succeed!")

    findAndOpenConversation(driver, privateGroupName)

    wait(2, "Fetching data")

    while True:
        row_id = 0

        foundSomeMessageContainer = False
        while foundSomeMessageContainer == False:
            row_id = findLatestMessageFromChatList(driver, 3)
            if row_id != 0:
                foundSomeMessageContainer = True
                break

            row_id = findLatestMessageFromChatList(driver, 4)
            if row_id != 0:
                foundSomeMessageContainer = True
                break

            row_id = findLatestMessageFromChatList(driver, 5)
            if row_id != 0:
                foundSomeMessageContainer = True
                break

            row_id = findLatestMessageFromChatList(driver, 6)
            if row_id != 0:
                foundSomeMessageContainer = True
                break
            
            if row_id == 0:
                foundSomeMessageContainer = False
                wait(5, "Waiting to do other search")


        for i, roundGroups in enumerate(slices):
            print(f"\nRound {i} running!")

            if i != 0:
                findAndOpenConversation(driver, privateGroupName)

            forwardMessageByRound(driver, row_id, roundGroups)

        # didDeleteMessage = False
        # while didDeleteMessage == False:
        #     try:
        #         deleteMessageById(driver, row_id, privateGroupName)
        #         didDeleteMessage = True
        #     except:
        #         wait(2, "Something wrong happen while deleting message")


def findLatestMessageFromChatList(driver: webdriver, id: int) -> int:
    try:
        print(f"Trying with ID : {id}")

        element = driver.find_element(
            By.CSS_SELECTOR, f"#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child({id}) > div > div")

        data_test_id = element.get_attribute("data-testid")
        print(data_test_id)

        if "msg-container" in data_test_id:
            return id
    except:
        return 0


def selectGroupsFromForwardModal(driver: webdriver, groups: list[str]):
    _searchbar = driver.find_element(
        By.CSS_SELECTOR, "#app > div > span:nth-child(2) > div > div > div > div > div > div > div > div:nth-child(2) > div > div > div._2vDPL > div > div.Er7QU.copyable-text.selectable-text")

    for groupName in groups:
        _searchbar.click()
        _searchbar.clear()
        _searchbar.send_keys(groupName)

        wait(2, "Waiting to get groups")

        # _firstGroupFromList
        driver.find_element(
            By.XPATH, "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button"
        ).click()

    return


def deleteMessageById(driver: webdriver, row_id: int, privateGroupName: str):
    findAndOpenConversation(driver, privateGroupName)
    wait(5, "Preparing to delete message")

    # threeDotsButton
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/div/span").click()

    # selectMessagesOption
    k = 2
    foundSelectMessagesBtn = False
    while foundSelectMessagesBtn == False:
        element = driver.find_element(
            By.CSS_SELECTOR, f"#app > div > span:nth-child(4) > div > ul > div > div > li:nth-child({k}) > div")
        
        if "mi-select-messages" in element.get_attribute("data-testid"):
            element.click()
            foundSelectMessagesBtn = True
        else:
            wait(2, "Select messages btn not found")
            k += 1

    # messageDiv
    driver.find_element(
        By.CSS_SELECTOR, f"#main > div._2gzeB > div > div._1Y114._5kRIK > div.n5hs2j7m.oq31bsqd.lqec2n0o.eu5j4lnj > div:nth-child({row_id})").click()

    # trash button
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div[4]/div/span[2]/div/button[2]/span"
    )

    # confirm button
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div[2]/div/div"
    )


def forwardMessageByRound(driver: webdriver, row_id: int, groupNames: list[str]):
    jsSelector = f"#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child({row_id}) > div > div > div.p357zi0d.ktfrpxia.nu7pwgvd.fhf7t426.sap93d0t.gndfcl4n._1m68F > div:nth-child(1)"
    rightForwardButton = driver.find_element(By.CSS_SELECTOR, jsSelector)
    rightForwardButton.click()

    selectGroupsFromForwardModal(driver, groupNames)

    wait(5, "Waiting to submit messages")

    didSubmit = False
    while didSubmit == False:
        try:
            jsSelector = "#app > div > span:nth-child(2) > div > div > div > div > div > div > div > span > div > div > div"
            submitButton = driver.find_element(By.CSS_SELECTOR, jsSelector)
            submitButton.click()
            didSubmit = True
        except:
            wait(2, "Some error occurred while sending message")

    wait(5, "Waiting to submit messages")

    try:
        element = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/span[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div")
        data_test_id = element.get_attribute("data-testid")
        if "confirm-popup" in data_test_id:
            element.click()
    except:
        print("Confirm pop wasn't shown")
    finally:
        return


if __name__ == "__main__":
    main()

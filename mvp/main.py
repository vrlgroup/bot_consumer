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
            k = 1
            while k <= 6:
                wait(1, "Waiting...")
                row_id = findLatestMessageFromChatList(driver, k)
                if row_id != 0 and row_id != None:
                    foundSomeMessageContainer = True
                    break
                else:
                    k += 1

            if row_id == 0:
                foundSomeMessageContainer = False
                wait(5, "Waiting to do other search")
            else:
                foundSomeMessageContainer = True
                break
 
        for i, roundGroups in enumerate(slices):
            print(f"\nRound {i} running!")

            if i != 0:
                findAndOpenConversation(driver, privateGroupName)

            forwardMessageByRound(driver, row_id, roundGroups)

        didDeleteMessage = False
        while didDeleteMessage == False:
            try:
                deleteMessageById(driver, row_id, privateGroupName)
                didDeleteMessage = True
                break
            except:
                wait(2, "Something wrong happen while deleting message")



def findLatestMessageFromChatList(driver: webdriver, id: int) -> int:
    try:
        print(f"Trying with ID : {id}")

        selector = f"#main > div._2gzeB > div > div._5kRIK > div.n5hs2j7m.oq31bsqd.gx1rr48f.qh5tioqs > div:nth-child({id}) > div > div > div"

        element = driver.find_element(By.CSS_SELECTOR, selector)
        data_test_id = element.get_attribute("data-testid")
        
        if "msg-container" in data_test_id:
            print(f"Founded! {id}")
            return id
    except:
        return 0


def selectGroupsFromForwardModal(driver: webdriver, groups: list[str]):
    _searchbar = driver.find_element(By.XPATH, "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/p")

    for groupName in groups:
        _searchbar.click()
        _searchbar.send_keys(groupName)
        wait(2, "Waiting to get groups")

        # firstGroupFromList
        driver.find_element(By.XPATH, "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button/div[2]/div").click()
        
        _searchbar.send_keys(Keys.CONTROL, "a")
        _searchbar.send_keys(Keys.BACKSPACE)
    return


def deleteMessageById(driver: webdriver, _: int, privateGroupName: str):
    findAndOpenConversation(driver, privateGroupName)
    wait(5, "Preparing to delete message")

    row_id = 0
    foundSomeMessageContainer = False
    while foundSomeMessageContainer == False:
        k = 1
        while k <= 6:
            wait(1, "Waiting...")
            row_id = findLatestMessageFromChatList(driver, k)
            if row_id != 0 and row_id != None:
                foundSomeMessageContainer = True
                break
            else:
                k += 1

        if row_id == 0:
            foundSomeMessageContainer = False
            wait(5, "Waiting to do other search")
        else:
            foundSomeMessageContainer = True
            break

    openSelectMessages(driver)
    didSelectMsg = False
    while didSelectMsg == False:
        wait(1, "Waiting...")
        selector = f"/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{row_id}]/div/div/span/div/div"
        try:
            driver.find_element(By.XPATH, selector).click()
            didSelectMsg = True
            break
        except:
            print(f"Error while selecting msg {row_id}")
            didSelectMsg = False

    didClickToDelete = False
    while didClickToDelete == False:
        k = 1
        while k <= 5:
            selector = f"/html/body/div[1]/div/div/div[4]/div/span[2]/div/button[{k}]/span"
            try:
                el = driver.find_element(By.XPATH, selector)
                if "delete" in el.get_attribute("data-testid"):
                    el.click()
                    didClickToDelete = True
                    break
                else:
                    didClickToDelete = False
                    k += 1
            except:
                print("Fail to click to forward msgs")
                didClickToDelete = False
                k+=1
        

    didConfirm = False
    while didConfirm == False:
        k = 1
        while k <= 2:
            el = driver.find_element(By.XPATH, f"/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div[{k}]/div")
            
            if "popup-controls-delete" in el.get_attribute("data-testid"):
                el.click()
                didConfirm = True
                break

            k += 1



def clickGroupThreeDots(driver : webdriver):
    selector = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/div/span"
    driver.find_element(By.XPATH, selector).click()

def openSelectMessages(driver : webdriver) :
    clickGroupThreeDots(driver)

    k = 1
    while k <= 5:
        selector = f"/html/body/div[1]/div/span[4]/div/ul/div/div/li[{k}]"
        try:
            el = driver.find_element(By.XPATH, selector)
            if "mi-select-messages" in el.get_attribute("data-testid"):
                el.click()
                wait(1, "Waiting to change page state, for select messages")
                break
        except:
            k+=1

def forwardMessageByRound(driver: webdriver, row_id: int, groupNames: list[str]):
    openSelectMessages(driver)

    didSelectMsg = False
    while didSelectMsg == False:
        wait(1, "Waiting...")
        selector = f"/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{row_id}]/div/div/span/div/div"
        try:
            driver.find_element(By.XPATH, selector).click()
            didSelectMsg = True
            break
        except:
            print(f"Error while selecting msg {row_id}")
            didSelectMsg = False

    didClickToForward = False
    while didClickToForward == False:
        k = 1
        while k <= 5:
            selector = f"/html/body/div[1]/div/div/div[4]/div/span[2]/div/button[{k}]/span"
            try:
                el = driver.find_element(By.XPATH, selector)
                if "forward" in el.get_attribute("data-testid"):
                    el.click()
                    didClickToForward = True
                    break
                else:
                    didClickToForward = False
            except:
                print("Fail to click to forward msgs")
                didClickToForward = False

            k+=1
        

    selectGroupsFromForwardModal(driver, groupNames)

    wait(5, "Waiting to submit messages")

    didSubmit = False
    while didSubmit == False:
        try:
            xp = "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div"
            submitButton = driver.find_element(By.XPATH, xp)
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

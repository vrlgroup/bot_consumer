from selenium.webdriver.chrome.service import Service

def configureDriver(path: str):
    return Service(executable_path=path)
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_ios.gesture_login import test_login_pass
import time

def test_webview(driver):
    driver.find_element('accessibility id', 'nav_Web-View').click()
    print(f'available contexts before/during loaders: {driver.contexts}')

    WebDriverWait(driver,15).until(lambda d: any('WEBVIEW' in ctx for ctx in d.contexts))
    print(f'available contexts after loaders {driver.contexts}')

    for ctx in driver.contexts:
        if 'WEBVIEW' in ctx:
            driver.switch_to.context(ctx)
            print(f'Switched to "{ctx}" context')
            break    

    WebDriverWait(driver,10).until(EC.element_to_be_clickable([AppiumBy.CSS_SELECTOR,'#login_field'])).send_keys('aravindbadiger@gmail.com')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable([AppiumBy.CSS_SELECTOR,'#password'])).send_keys('gitpwd')

    WebDriverWait(driver,5).until(EC.element_to_be_clickable([AppiumBy.XPATH,'/html/body/div[1]/div[3]/main/div/div[2]/form/div[3]/input'])).click()



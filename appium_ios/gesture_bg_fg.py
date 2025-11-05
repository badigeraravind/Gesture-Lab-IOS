from appium_ios.gesture_login import test_login_pass
import time

def test_bg_fg(driver):
    driver.find_element('accessibility id', 'nav_No_Internet').click()
    driver.background_app(5)
    driver.activate_app('com.apple.news')
    time.sleep(3)
    driver.activate_app('com.badigeraravinda.GestureLabIOS')


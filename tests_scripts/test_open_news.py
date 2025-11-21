from appium import webdriver
from appium.options.ios import XCUITestOptions
import time

def open_news():
    o = XCUITestOptions()
    o.platform_name   = "iOS"
    o.platformVersion = "18.1"
    o.deviceName      = "iPhone 16 Pro"
    o.udid            = "8873047A-A7E8-4EA3-9880-15DAE2AB47A6"
    o.automationName  = "XCUITest"
    o.bundleId        = "com.apple.news"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=o)
    try:
        driver.activate_app("com.apple.news")
        time.sleep(2)
        info = driver.execute_script("mobile: activeAppInfo")
        print("ACTIVE APP:", info)
    finally:
        driver.quit()

if __name__ == "__main__":
    open_news()
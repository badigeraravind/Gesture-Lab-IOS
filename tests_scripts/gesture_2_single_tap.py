
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

def test_single_tap(driver):
    print('== Testing Single Tap Flow ==')
    #time.sleep(5)
    #driver.execute_script('mobile: alert',{'action':'accept'})
   
    WebDriverWait(driver,10).until(EC.element_to_be_clickable([AppiumBy.ACCESSIBILITY_ID,'nav_Single_Tap'])).click()
    #driver.find_element('accessibility id','nav_Single_Tap').click()

    #assuming we are interacting with the dynamic element inside gameplay.
    rect = driver.find_element('accessibility id', 'btn_switch_on').rect
    print(rect)
    btnx = int(rect['x'] + rect['width'] / 2)
    btny = int(rect['y'] + rect['height'] / 2)
    driver.execute_script('mobile: tap', {'x':btnx, 'y':btny})
    time.sleep(5)
    print('Light Bulb Is Turned On')
    time.sleep(3)
    driver.find_element('accessibility id','Home').click()

    
    



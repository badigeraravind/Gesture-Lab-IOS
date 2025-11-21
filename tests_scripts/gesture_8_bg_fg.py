import time

def test_bg_fg(driver):
    driver.find_element('accessibility id', 'nav_No_Internet').click()
    #driver.background_app(5)
    driver.activate_app('com.apple.news')
    time.sleep(3)
    driver.activate_app('com.badigeraravinda.GestureLabIOS')
    #driver.find_element('accessibility id','')
    time.sleep(3)
    driver.find_element('accessibility id','Home').click()


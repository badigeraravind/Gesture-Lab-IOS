import time

def test_double_tap(driver):
    print('== Testing Double Tap Flow ==')
    driver.find_element('accessibility id', 'nav_Double_Tap').click()
    
    size = driver.get_window_size()
    print(size)
    tapx = size['width'] * 0.5
    tapy = size['height'] * 0.29
    driver.execute_script('mobile: doubleTap', {'x':tapx, 'y': tapy})
    print('double tapped, teddy should spin')
    time.sleep(5)
    driver.execute_script('mobile: doubleTap', {'x':tapx, 'y': tapy})
    print('double tapped, teddy should not spin')
    time.sleep(3)
    driver.find_element('accessibility id','Home').click()
    


    # or if element is shown in ui hirarchy
    #a = driver.find_element('accessibility id','toy_box')
    #driver.execute_script('mobile: doubleTap', {'element':a.id})

    




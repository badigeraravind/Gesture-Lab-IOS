import time

def test_internet(driver):
    driver.find_element('accessibility id','nav_No_Internet').click()
    a = driver.find_element('-ios predicate string', 'name == "no_internet" AND label == "Simulate network loss"').rect
    print(a)
    btnx = int(a['x'] + a['width'] / 2)
    btny = int(a['y'] + a['height'] / 2)
    driver.execute_script('mobile: tap', {'x':btnx , 'y':btny})
    print('no internet simulation started')
    time.sleep(3)

    size = driver.get_window_size()
    stpx = size['width'] * 0.5
    stpy = size['height'] * 0.69
    driver.execute_script('mobile: tap', {'x':btnx , 'y':btny})
    print('simulation stopped')


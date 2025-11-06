import time

def test_zoom_out(driver):
    driver.find_element('accessibility id','nav_Multi-Touch').click()
    map = driver.find_element('accessibility id', 'world_map')
    driver.execute_script('mobile: pinch', {'scale':0.5, 'velocity': -0.3, 'element': map.id})
    time.sleep(3)

def test_zoom_in(driver):
    map = driver.find_element('accessibility id', 'world_map')
    driver.execute_script('mobile: pinch', {'scale':3, 'velocity': 3, 'element': map.id})
    time.sleep(3)
    driver.find_element('accessibility id','Home').click()

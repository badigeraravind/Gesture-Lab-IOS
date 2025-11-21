import random
import time
def test_scroll(driver):
    driver.find_element('accessibility id','nav_Swipe/Scroll').click()
    scroll_el = driver.find_element('accessibility id','scroll_list')

    for i in range(1,4):
        dir = random.choice(['up','down'])
        driver.execute_script('mobile: scroll', {'element':scroll_el, 'direction':dir})
        print(f'scrolled {dir} direction')
    time.sleep(3)
    driver.find_element('accessibility id','Home').click()

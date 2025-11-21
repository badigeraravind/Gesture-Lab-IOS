import random
def test_swipe(driver):
    driver.find_element('accessibility id','nav_Swipe/Scroll').click()
    swipe_el = driver.find_element('-ios class chain','**/XCUIElementTypeCollectionView[`name == "swipe_pager"`]')

    for _ in range(1,4):
        dir = random.choice(['left','right'])
        driver.execute_script('mobile: swipe',{'element':swipe_el, 'direction':dir})
        print(f'Swiped {dir} direction')

    


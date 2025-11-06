
def test_tap_n_hold(driver):
    driver.find_element('accessibility id', 'nav_Tap_and_Hold').click()

    a = driver.find_element('accessibility id', 'btn_preview')

    driver.execute_script('mobile: touchAndHold',{'element':a.id, 'duration':5.0})

    print('Tapped and Held, Gift Box should reveal')

    driver.find_element('accessibility id','Home').click()


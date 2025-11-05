import time

def test_login_pass(driver):
    print('== Testing Login Pass Flow =="')
    uname = driver.find_element('accessibility id','username_field')
    uname.send_keys('truenamehoood')
    pwd = driver.find_element('accessibility id', 'password_field')
    pwd.send_keys('true@902')

    driver.find_element('accessibility id','login_button').click()

def _test_login_fail_retry(driver):
    print('== Testing Login Fail Retry Pass Flow =="')
    uname = driver.find_element('accessibility id', 'username_field')
    uname.send_keys('falsename')
    pwd = driver.find_element('accessibility id', 'password_field')
    pwd.send_keys('false@902')

    driver.find_element('accessibility id', 'login_button').click()

    uname.clear()
    uname.send_keys('baddy')                #or uname.set_value('your text')
    pwd.clear()
    pwd.send_keys('123')

    driver.find_element('accessibility id', 'login_button').click()

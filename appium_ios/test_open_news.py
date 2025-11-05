
def test_open_news(driver):
    driver.activate_app("com.apple.news")
    info = driver.execute_script("mobile: activeAppInfo")
    print("\nActive App: ", info)
    assert info.get("bundleId") == "com.apple.news"
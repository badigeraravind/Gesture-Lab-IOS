from appium import webdriver
from appium.options.ios import XCUITestOptions


def create_driver():
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.platformVersion = "18.1"
    options.deviceName = "iPhone 16 Pro"  # match your simulator name exactly
    options.udid = "8873047A-A7E8-4EA3-9880-15DAE2AB47A6"
    options.bundleId = "com.apple.Preferences"  # Settings app

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver


def test_open_settings():
    driver = create_driver()
    try:
        # Force-open Settings after WDA starts
        driver.activate_app("com.apple.Preferences")
        # Optional: wait a moment for UI to settle
        import time
        time.sleep(1.5)
        # Confirm Settings is the active foreground app
        info = driver.execute_script("mobile: activeAppInfo")
        print("ACTIVE APP:", info)
        assert info.get("bundleId") == "com.apple.Preferences"
    finally:
        driver.quit()


if __name__ == "__main__":
    test_open_settings()
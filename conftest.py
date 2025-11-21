import os
import pytest
import time
import json
from appium import webdriver
from appium.options.ios import XCUITestOptions

@pytest.fixture(scope = 'session')

def driver():
    o = XCUITestOptions()
    o.platform_name = "iOS"
    o.platform_version = os.environ.get('IOS PLATFORM VERSION','18.1')
    o.device_name = os.environ.get("IOS_DEVICE_NAME","iPhone 16 Pro")
    o.udid = os.environ.get('SIM_UDID')
    #o.udid = "5F0B82D6-F318-4CE1-804B-6152B0DCAA6F"
    o.automation_name = "XCUITest"
    app_path = os.environ.get('APP_PATH', os.path.join(os.getcwd(), 'GestureLabIOS', 'build', 'Build', 'Products', 'Debug-iphonesimulator', 'GestureLabIOS.app'),)
    #o.app = "/Users/aravindbadiger/game-qa-python-lab/GestureLabIOS/build/Build/Products/Debug-iphonesimulator"
    print("Using app path:", app_path)
    if not os.path.exists(app_path):
        raise RuntimeError(f"App not found at {app_path} — build it or set APP_PATH env var correctly.")
    o.app = app_path
    o.bundle_id = "com.badigeraravinda.GestureLabIOS"
    o.no_reset = False
    o.show_xcode_log = True
    o.use_new_wda = False
    #o.auto_accept_alerts = True
    o.wda_launch_timeout = 60000
    o.wda_connection_timeout = 60000
    
    o.set_capability(
        'appium:permissions', 
        json.dumps({
            'com.badigeraravinda.GestureLabIOS':{
                'camera' : 'yes',
                'location' : 'yes',
                'photos' : 'yes',
                'notifications': 'yes'
            }
        })
    )
    # o.xcodeOrgId      = "<Your Apple Team ID>"       # required for real device
    # o.xcodeSigningId  = "iPhone Developer"

    dvr = webdriver.Remote("http://127.0.0.1:4723", options = o)
    print('Setup Fixture')

    yield dvr
    
    print('Teardown Fixture')
    dvr.quit()
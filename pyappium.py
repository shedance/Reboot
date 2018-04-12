from appium import webdriver
import time
#字典配置测试设备信息相关
desired_cap = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '4.4',
    'appPackage': 'com.android.calculator2',
    'appActivity':'com.android.calculator2.Calculator'
}
#初始化链接到设备webdriver.remote
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
time.sleep()
driver.find_element_by_name('7').click()
driver.find_element_by_name('+').click()
driver.find_element_by_name('1').click()
driver.find_element_by_name('3').click()
driver.find_element_by_name('=').click()

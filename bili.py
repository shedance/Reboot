from appium import webdriver
import time
import HTMLTestRunner
import unittest

class bili(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "deviceName": "0123456789ABCDEF",
            "platformName": "Android",
            "platformVersion": "6.0",
            "appPackage": "tv.danmaku.bili",
            "appActivity": "tv.danmaku.bili.ui.splash.SplashActivity"
            }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def bl(self):
        time.sleep(10)
        self.driver.find_element_by_id('tv.danmaku.bili:id/avatar_layout').click()
        time.sleep(10)
        self.driver.find_element_by_id('tv.danmaku.bili:id/avatar_layout').click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()


if __name__ == "__main__":
    test = unittest.TestSuite()
    test.addTest(bili("bl"))
    file_path = "F:\\MerciGo\\Reports\\result2.html"
    file_result = open(file_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = "哔哩哔哩xpath")
    runner.run(test)
    file_result.close()
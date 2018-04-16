from appium import webdriver
import time
import HTMLTestRunner
import unittest
import os
import sys
class calculator(unittest.TestCase):

    def test_calculator1(self):
        # 字典配置测试设备信息相关
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '4.4',
            'appPackage': 'com.android.calculator2',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        # 初始化链接到设备webdriver.remote
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        time.sleep(5)
        driver.find_element_by_name('7').click()
        driver.find_element_by_name('+').click()
        driver.find_element_by_name('1').click()
        driver.find_element_by_name('3').click()
        driver.find_element_by_name('=').click()
        time.sleep(5)
    def test_calculator2(self):
        # 字典配置测试设备信息相关
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '4.4',
            'appPackage': 'com.android.calculator2',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        # 初始化链接到设备webdriver.remote
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        time.sleep(5)
        driver.find_element_by_name('5').click()
        driver.find_element_by_name('+').click()
        driver.find_element_by_name('1').click()
        driver.find_element_by_name('3').click()
        driver.find_element_by_name('=').click()
        time.sleep(5)
    def test_calculator3(self):
        # 字典配置测试设备信息相关
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '4.4',
            'appPackage': 'com.android.calculator2',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        # 初始化链接到设备webdriver.remote
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        time.sleep(5)
        driver.find_element_by_name('5').click()
        driver.find_element_by_name('+').click()
        driver.find_element_by_name('1').click()
        driver.find_element_by_name('5').click()
        driver.find_element_by_name('=').click()
        time.sleep(5)

if __name__=="__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例加到容器中
    test.addTest(calculator("test_calculator1"))
    test.addTest(calculator("test_calculator2"))
    test.addTest(calculator("test_calculator3"))



    #定义报告存放路径，支持相对路径
    file_path = "F:\\MerciGo\\Reports\\result.html"
    file_result = open(file_path, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title= "Calculator Test")


    #运行测试用例
    runner.run(test)
    file_result.close()
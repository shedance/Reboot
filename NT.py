import HTMLTestRunner
import unittest
from appium import webdriver
import time

class jisuanqi(unittest.TestCase):
    #执行用例前准备测试环境
    def setUp(self):
        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "platformVersion": "4.4",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        time.sleep(3)
    #用例执行完成后，清理状态，这里即关闭app
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
    #测试用例函数，编写测试用例
    def calculator(self):
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("+").click()
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("=").click()

#运行测试用例
if __name__ == "__main__":
    #定义测试用例的容器Test
    test = unittest.TestSuite()
    #将测试用例使用addTest装入容器中
    test.addTest(jisuanqi("calculator"))

    #测试用例执行结果报告文件路径
    file_path = "F:\\MerciGo\\Reports\\result.html"
    #测试结果报告html打开方式wb
    file_result = open(file_path,"wb")
    #测试用例执行后测试报告写入
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title= "计算器简单测试")
    #测试执行
    runner.run(test)
    #运行完成后close掉报告的html
    file_result.close()
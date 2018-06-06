import unittest
from appium import webdriver
import os

class AndroidMobileWebTest(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {
            'platformName': 'Android',
            #'platformVersion': '6.0',
            'deviceName': 'Android Emulator',
            'browserName': 'Chrome',
            #'avd': 'Pixel_XL_API_P',
            #'udid': 'emulator-5554',
        }
        self.driver = webdriver.Remote(
            command_executor= 'http://localhost:4723/wd/hub',
            desired_capabilities= desired_capabilities)

    def test_mobileweb(self):
        self.driver.get('http://www.google.com')
        self.driver.find_element_by_name('q').clear()
        self.driver.find_element_by_name('q').send_keys('Appium')
        self.driver.find_element_by_name('q').submit()
        appium = self.driver.find_element_by_link_text("Appium")
        appium.click()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidMobileWebTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

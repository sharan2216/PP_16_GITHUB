import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage


class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #login page object
        login=LoginPage(driver)
        login.enter_username("Admin")
        self.driver.implicitly_wait(5)
        login.enter_password("admin123")
        self.driver.implicitly_wait(5)
        login.click_Login()
        self.driver.implicitly_wait(5)

        #homepage object
        home=HomePage(driver)
        home.click_image()
        self.driver.implicitly_wait(5)
        home.click_logout()
        self.driver.implicitly_wait(5)



        # self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        # self.driver.implicitly_wait(5)
        # #username link
        # self.driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
        # # click logout
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
        # self.driver.implicitly_wait(5)
        # # time.sleep()


    @classmethod
    def teardown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



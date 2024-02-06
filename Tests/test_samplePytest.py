from selenium import webdriver

import time
from selenium.webdriver.common.by import By


class Test_Global:

    def test_Sample(self):
        global driver
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get("https://qavbox.github.io/demo/")
        title=driver.title
        print(title)
        assert "QAVBOX" in driver.title

    def test_navReg(self):
        driver.find_element(By.LINK_TEXT,"SignUp Form").click()
        driver.save_screenshot("SCREENSHOTS/SS.png")
        time.sleep(3)
        driver.quit()
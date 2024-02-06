from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Test_Actionkey:

    def test_javascript(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        username=driver.find_element(By.ID,"login1")
        password=driver.find_element(By.XPATH,"//input[@id='password']")
        act = ActionChains(driver)
        username.send_keys("selenium")

        time.sleep(2)

        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB).perform()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.ENTER).perform()




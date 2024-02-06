from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Test_Waits:

    def test_waits(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get("https://qavbox.github.io/demo/delay/")
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH,"//input[@name='commit']").click()

        assert 'Delay' in driver.title

        commit=driver.find_element(By.XPATH,"//input[@name='commit']")
        commit.click()
        # driver.implicitly_wait(30)
        time.sleep(6)
        el = driver.find_element(By.XPATH, "//h2[@id='two']")
        print("First Attempt - " + el.text)
        driver.implicitly_wait(30)
        delayele =driver.find_element(By.XPATH,"//label[contains(text(),'Click below button to display button (id=delay) & text after 5 sec')]")
        print(delayele.text)




        time.sleep(3)
        driver.quit()



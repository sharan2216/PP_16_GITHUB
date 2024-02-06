from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Test_Global:

    def test_webtable(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get("https://qavbox.github.io/demo/webtable/")
        title = driver.title
        print(title)
        assert "webtable" in driver.title
        print("----------------------------")

        table = driver.find_element(By.ID,'table01')
        # header=driver.find_elements(By.TAG_NAME,"th")
        body = driver.find_element(By.XPATH,"//table[@id='table01']//tbody")
        cells=driver.find_element(By.XPATH,"//table[@id='table01']//tbody/tr[1]/td[2]")
        rows = driver.find_elements(By.XPATH,"//table[@id='table01']//tbody/tr")
        cols= driver.find_elements(By.XPATH,"//table[@id='table01']//tbody/tr/td")
        # for cell in cells:
        #     print(cell.text)

        print(len(rows))

        driver.quit()

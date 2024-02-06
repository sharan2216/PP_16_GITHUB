from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
'''
   few comments added here
'''

class Test_Global:

    def test_Sample1(self):
        global driver
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.set_page_load_timeout(50)
        driver.get("https://qavbox.github.io/demo/signup/")
        title=driver.title
        print(title)
        assert "Registration" in driver.title

        gender = driver.find_element(By.XPATH,"//select[@name='sgender']")
        driver.execute_script("arguments[0].scrollIntoView();", gender)
        # time.sleep(3)
        select = Select(driver.find_element(By.XPATH,"//select[@name='sgender']"))
        select.select_by_value("female")
        # time.sleep(3)
        driver.implicitly_wait(10)
        print("\nselected item : "+ select.first_selected_option.text)
        assert "Female" in select.first_selected_option.text

        opts = select.options
        for opt in opts:
            print(opt.text)

        driver.quit()

    # def test_navReg(self):
    #     driver.find_element(By.LINK_TEXT,"SignUp Form").click()
    #     driver.save_screenshot("SCREENSHOTS/SS.png")
    #     time.sleep(3)
    #     driver.quit()
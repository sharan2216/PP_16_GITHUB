from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By


class HomePage():


    def __init__(self,driver):
        self.driver=driver

        self.image_xpath = "//p[@class='oxd-userdropdown-name']"
        self.logout_xpath = "//a[contains(text(),'Logout')]"


    def click_image(self):
        self.driver.find_element(By.XPATH,self.image_xpath).click()
        self.driver.implicitly_wait(5)

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()
        self.driver.implicitly_wait(5)





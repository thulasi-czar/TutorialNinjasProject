from selenium.webdriver.common.by import By

class HomePage:
    myAccount_drop_menu_xpath = "//a[@title='My Account']"
    login_link_text = "Login"
    register_link_text = "Register"

    def __init__(self,driver):
        self.driver = driver

    def click_on_myAccount_drop_menu(self):
        self.driver.find_element(By.XPATH,self.myAccount_drop_menu_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link_text).click()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_link_text).click()

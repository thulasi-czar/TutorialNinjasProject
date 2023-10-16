from selenium.webdriver.common.by import By
class LoginPage:
    username_field_box_xpath = "//input[@id='input-email']"
    password_field_box_xpath = "//input[@id='input-password']"
    login_btn_xpath = "//input[@value='Login']"

    def __init__(self,driver):
        self.driver = driver

    def get_page_title(self):
        title = self.driver.title
        return title

    def enter_userName(self,name):
        user_name_input_box = self.driver.find_element(By.XPATH,self.username_field_box_xpath)
        user_name_input_box.clear()
        user_name_input_box.send_keys(name)

    def enter_password(self,password):
        password_input_box = self.driver.find_element(By.XPATH,self.password_field_box_xpath)
        password_input_box.clear()
        password_input_box.send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_btn_xpath).click()



from selenium.webdriver.common.by import By

class RegisterPage:
    fn_field_box_xpath = "//input[@id='input-firstname']"
    ln_field_box_xpath = "//input[@id='input-lastname']"
    email_field_box_xpath = "//input[@id='input-email']"
    telephone_field_box_xpath = "//input[@id='input-telephone']"
    password_field_box_xpath = "//input[@id='input-password']"
    pswd_cnf_field_box_xpath = "//input[@id='input-confirm']"
    subscrb_radio_btn_no_xpath = "//input[@name='newsletter' and @value='0']"
    subscrb_radio_btn_yes_xpath = "//input[@name='newsletter' and @value='1']"
    agree_checkbox_xpath = "//input[@name='agree']"
    continue_btn_xpath = "//input[@value='Continue']"

    def __init__(self,driver):
        self.driver = driver

    def enter_firstName(self,name):
        fn_fieldbox_element = self.driver.find_element(By.XPATH,self.fn_field_box_xpath)
        fn_fieldbox_element.clear()
        fn_fieldbox_element.send_keys(name)

    def enter_lastName(self,name):
        ln_fieldbox_element = self.driver.find_element(By.XPATH,self.ln_field_box_xpath)
        ln_fieldbox_element.clear()
        ln_fieldbox_element.send_keys(name)

    def enter_email(self,email):
        email_fieldbox_element = self.driver.find_element(By.XPATH,self.email_field_box_xpath)
        email_fieldbox_element.clear()
        email_fieldbox_element.send_keys(email)

    def enter_telephone_num(self,number):
        tel_num_fieldbox_element = self.driver.find_element(By.XPATH,self.telephone_field_box_xpath)
        tel_num_fieldbox_element.clear()
        tel_num_fieldbox_element.send_keys(number)

    def enter_password(self,password):
        password_fieldbox_element = self.driver.find_element(By.XPATH,self.password_field_box_xpath)
        password_fieldbox_element.clear()
        password_fieldbox_element.send_keys(password)

    def reEnter_password(self,password):
        password_fieldbox_element = self.driver.find_element(By.XPATH, self.pswd_cnf_field_box_xpath)
        password_fieldbox_element.clear()
        password_fieldbox_element.send_keys(password)

    def subscription_option(self,choice):
        if choice.lower() == "yes":
            self.driver.find_element(By.XPATH,self.subscrb_radio_btn_yes_xpath).click()
        elif choice.lower() == "no":
            self.driver.find_element(By.XPATH,self.subscrb_radio_btn_no_xpath).click()

    def click_on_agree_checkbox(self):
        self.driver.find_element(By.XPATH, self.agree_checkbox_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()



import pytest
from pageObjects.home_page import HomePage
from pageObjects.register_page import RegisterPage
from utilities.customLogger import LogGenerator
from utilities.readConfigurations import ReadConfig
import time
import allure

@pytest.mark.usefixtures("setup_teardown")
class Test_002_Register:
    logger = LogGenerator.gen_logs()
    url = ReadConfig.get_url()

    logger.info("******************** Test_002_Register ***********************")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_register_with_mandatory_fields(self):
        self.logger.info("************* test case register with mandatory fields started **************")
        self.driver.get(self.url)
        home_page = HomePage(self.driver)
        home_page.click_on_myAccount_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_firstName("thulasi")
        register_page.enter_lastName("ashok")
        register_page.enter_email(self.generate_email())
        register_page.enter_telephone_num("1234567890")
        register_page.enter_password("ashok1234")
        register_page.reEnter_password("ashok1234")
        register_page.subscription_option("no")
        register_page.click_on_agree_checkbox()
        time.sleep(5)
        register_page.click_on_continue_button()
        self.logger.info("************* test case register with mandatory fields finished **************")


    def generate_email(self):
        name = "thulasi#"
        formatted_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        email = name + formatted_time + "@gmail.com"
        return  email

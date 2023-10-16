import pytest
from utilities.customLogger import LogGenerator
from utilities.readConfigurations import ReadConfig
from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
import softest

@pytest.mark.usefixtures("setup_teardown")
class Test_001_Login(softest.TestCase):
    url = ReadConfig.get_url()
    logger = LogGenerator.gen_logs()
    username = ReadConfig.get_userName()
    password = ReadConfig.get_password()
    logger.info("----------------this is Test_001_Login----------------------")

    @pytest.mark.regression
    def test_login_with_valid_credentials(self):
        self.driver.get(self.url)
        self.homePage = HomePage(self.driver)
        self.homePage.click_on_myAccount_drop_menu()
        self.homePage.select_login_option()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_userName(self.username)
        self.loginPage.enter_password(self.password)
        self.loginPage.click_on_login_button()


    @pytest.mark.smoke
    def test_login_with_invalid_credentials(self):
        self.driver.get(self.url)
        self.homePage = HomePage(self.driver)
        self.homePage.click_on_myAccount_drop_menu()
        self.homePage.select_login_option()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_userName('thulasi')
        self.loginPage.enter_password(self.password)
        self.loginPage.click_on_login_button()
        expected_title = "Account Login"
        actual_title = self.driver.title
        assert actual_title.__eq__(expected_title)
        # self.soft_assert(self.assertEquals,actual_title,expected_title)
        # self.assert_all()
        # print("this is after soft assertion fails")
        # self.driver.get("http://www.google.com")

from configparser import  ConfigParser

config = ConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    category = "basic info"

    @staticmethod
    def get_browser():
        browser = config.get(ReadConfig.category,"browser")
        return browser

    @staticmethod
    def get_url():
        url = config.get(ReadConfig.category,"url")
        return url

    @staticmethod
    def get_userName():
        user_name = config.get(ReadConfig.category,"userName")
        return user_name

    @staticmethod
    def get_password():
        password = config.get(ReadConfig.category,"password")
        return password

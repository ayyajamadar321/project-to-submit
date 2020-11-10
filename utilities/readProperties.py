import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\account.test\\PycharmProjects\\ISchoolConnect\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'passworrd')
        return password

    @staticmethod
    def getName():
        name = config.get('common info', 'name')
        return name

    @staticmethod
    def getLastName():
        lastname = config.get('common info', 'lastname')
        return lastname

    @staticmethod
    def getPhoneNo():
        phonenumber = config.get('common info', 'phonenumber')
        return phonenumber

    @staticmethod                                                   # Fetch data for dashboard form config file
    def get_oldUsername():
        old_username = config.get('common info', 'old_username')
        return old_username

    @staticmethod                                                   # Fetch data for dashboard form config file
    def get_oldPassword():
        old_passworrd = config.get('common info', 'old_passworrd')
        return old_passworrd
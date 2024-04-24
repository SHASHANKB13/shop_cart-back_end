import configparser


def init():
    CONFIG = r'/Users/shashank/Documents/python_projects/shopping_app_api/data.properties'
    config = configparser.ConfigParser()
    config.read(CONFIG)
    return config

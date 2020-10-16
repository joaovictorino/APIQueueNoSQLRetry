import configparser

config = configparser.ConfigParser()
config.read("config.ini")

app = None

def getAddressQueue():
    if config is not None:
        return config['DEFAULT']['rabbitmq']

def getAddressDB():
    if config is not None:
        return config['DEFAULT']['mongodb']

def getAddressStock():
    if config is not None:
        return config['DEFAULT']['stock']
import configparser

CONFIG_FILE = 'config/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

def listDomains():
    return config.sections()


def listKeys(domain):
    return config[domain]


def asString(domain, key) -> str:
    return config[domain][key]


def asInteger(domain, key) -> int:
    return config[domain].getint(key)


def asBoolean(domain, key) -> bool:
    return config[domain].getboolean(key)

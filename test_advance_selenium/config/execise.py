from configparser import ConfigParser

def config(filename):

    a=ConfigParser()
    a.read(filename,encoding="utf8")
    print(a.options('loggers'))
    print(a.items('loggers'))
    print(a.get("loggers","keys"))
    # print(a.)
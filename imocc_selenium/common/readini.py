from configparser import ConfigParser
class ReadIni():
    def __init__(self,filename,node):
        self.config=ConfigParser()
        self.config.read(filename)
        self.node=node


    def get_data(self,key):
        data = self.config.get(self.node,key)
        return data


if __name__=="__main__":
    a=ReadIni("../config/element_ini.ini","RegisterElement")
    print(a.node)
    print(a.config.sections())
    print(a.get_data("username"))
    print("abc")


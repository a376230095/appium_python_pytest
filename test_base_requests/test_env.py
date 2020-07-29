import requests
import yaml

class TestEnv():
    #一切的宗旨都是不能在代码中有数据的产生，这里就让ip环境变成了数据驱动
    with open("env.yml",encoding="UTF-8") as f:
        #让env成为dict类型方便编程
        """
        default: test
        testing-studio:
        test: 127.0.0.1
        dev: 127.0.0.2
        """
        #env就顺利成为了字典了
        env:dict=yaml.safe_load(f)

    #封装我们请求的方法、url、头部信息
    data={
        "method":"get",
        "url":"http://testing-studio.com/demo.txt",
        "headers":None
    }

    def send(self):
        #我们需要把写死的url写活，把域名改为ip地址，replace是返回一个值，所以需要赋值运算
        #我们去url只需要改yaml中defaul的值即可，就无须修改我们整体代码了
        self.data["url"]=self.data["url"].replace("testing-studio.com",self.env["testing-studio"][self.env["default"]])
        #打印出我们的data类型，验证我们的url结果
        print(self.data)
        #封装我们的requests函数
        r=requests.request(self.data["method"],self.data["url"],headers=self.data["headers"])

    def test_env(self):
        #执行我们的send函数
        self.send()
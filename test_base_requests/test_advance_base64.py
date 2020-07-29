import json
import requests
import base64

class TestAuthorize():
    #定义一个数据，里面有方法、url、header、和解密的方法
    data={
        "method":"get",
        "url":"http://127.0.0.1:8888/demo.txt",
        "headers":None,
        "encoding":"base64"
    }
    def send(self):
        #这里的request第一个传方法、第二个传urk、第三个随便传data、headers、cookies都行
        r=requests.request(self.data["method"],self.data["url"],headers=self.data["headers"])
        #当我们要解密的方法是base64，就执行base64操作
        if self.data["encoding"]=="base64":
            res=json.loads(base64.b64decode(r.text))
            print(res)
        #把加密过后的响应值发给第三方服务器，让第三方服务器解密之后返回解密过后的信息
        #确保解密过程没有人知道
        elif self.data["encoding"]=="private":
            return requests.post("url",data=r.content)

    def test_advance_base64(self):
        #执行send方法
        self.send()
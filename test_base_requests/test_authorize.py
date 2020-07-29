import requests
from requests.auth import HTTPBasicAuth

class TestAuthorize():
    def test_authorize(self):
        url="http://httpbin.testing-studio.com/basic-auth/user/tongtong"
        #需要传入auth=HTTPBasicAuth，后面是账号和密码
        r=requests.get(url=url,auth=HTTPBasicAuth("user","tongtong"))
        print(r.text)
import base64
import json
import requests

def test_base64():
    #这是本地建立的python -m http.server 8888
    #我放在了D盘，确保没有权限问题
    url="http://127.0.0.1:8888/demo.txt"
    r = requests.get(url=url)
    #如果不用json，解析出来的会有很多\n,用这个转化成字典好看一点
    #解密就用base64.b64decode，这里text和content都ok
    res=json.loads(base64.b64decode(r.text))
    #打印出解密base64的json文件
    print(res)
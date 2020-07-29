import requests

class TestCookies():
    def test_cookies_headers(self):
        url="http://httpbin.testing-studio.com/cookies"
        #headers是可以直接传cookie
        headers={
            #Cookie的写法，没有s，里面传的是键值对
            #传输的方法是"a=b;c=d"的传值方式
            "Cookie":"Cookie:BAIDUID=0FD996SDFG12107B9C227F4C:FG=1; locale=zh; bdshare_firstime=1384567418140;",
            "User-Agent":"Iphone"
        }
        r= requests.get(url=url,headers=headers)
        #这里打印头部需要request.headers
        print(r.request.headers)
        #打印出响应体的内容
        print(r.text)

    def test_cookies_dict(self):
        url = "http://httpbin.testing-studio.com/cookies"
        headers = {
            "User-Agent": "Iphone"
        }
        #创建一个字典，传入cookies
        cookies_data={
            "tongtong":"haha",
            "zeng":"gun"
        }
        #
        r=requests.get(url=url,headers=headers,cookies=cookies_data)
        #这里打印头部需要request.headers
        print(r.request.headers)
        #打印出响应体的内容
        print(r.text)

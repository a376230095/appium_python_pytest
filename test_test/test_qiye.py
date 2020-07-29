import requests
import pytest
import yaml


class Test_Contact():
    def test_a(self):
        #获取到access_token(正常的情况)
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww630f49269e06f865&corpsecret=YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        r=requests.get(url=url)
        access_token=r.json()["access_token"]
        print(access_token)
        assert r.json()["errcode"] == 0

    #获取access_token
    @pytest.mark.parametrize("corpid,corpsecret,result",yaml.safe_load(open("access_token.yml",encoding="UTF-8")))
    def test_b(self,corpid,corpsecret,result):
        # 获取到access_token(异常的情况)
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.text)
        assert r.json()["errcode"] == result
        # access_token = r.json()["access_token"]
        # print(access_token)
        # assert r.json()["errcode"] == 1

    #通讯录id为空
    def test_c(self):
        # 获取到access_token(异常的情况)
        corpid = "ww630f49269e06f865"
        corpsecret=""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.text)
        assert r.json()["errcode"] == 41004
        # access_token = r.json()["access_token"]
        # print(access_token)
        # assert r.json()["errcode"] == 1


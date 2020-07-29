import requests

from test_weixin_requests.api.base_api import Base_api
class Wework(Base_api):
    _corpid="ww630f49269e06f865"

    def get_token(self,corpsecret):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid":self._corpid,
                "corpsecret":corpsecret
            }
        }
        r =self.send(data)
        return r["access_token"]
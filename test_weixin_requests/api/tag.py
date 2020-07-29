import json

from api.base_api import Base_api
from api.wework import Wework


class Tag(Base_api):
    secret = "MDe1km8BK3AZ05Dnfw4uILuKCZDStZ2NPaokf-UE6c8"
    token = Wework().get_token(secret)
    def add(self,tag_name):
        # data={
        #     "method":"post",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        #     "params":{"access_token":f"{self.token}"},
        #     "json":{
        #         "group_name": "test",
        #         "tag":[{"name": f"{tag_name}"}]
        #     }

        # data=self.load("../data/tag_add.yml")
        # data["params"]["access_token"]=self.token
        # data["json"]["tag"][0]["name"]=tag_name
        # print(json.dumps(data,indent=2))
        # return self.send(data)

        data=self.template("../data/tag_add.yml",{"token":self.token,"tag_name":tag_name})
        return self.send(data)



    def get(self):
        token = Wework().get_token(self.secret)

        # data = {
        #     "method": "post",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        #     "params": {"access_token": f"{token}"},
        # }
        data=self.load("../data/tag_get.yml")
        data["params"]["access_token"]=self.token
        return self.send(data)

    def delete(self,tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": f"{self.token}"},
            "json":{
                "tag_id":[f"{tag_id}"]
            }
        }
        return self.send(data)

    def update(self,tag_id,tag_name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": f"{self.token}"},
            "json":{
                "id":f"{tag_id}",
                "name":f"{tag_name}"
            }
        }
        return self.send(data)
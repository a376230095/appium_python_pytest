import json

import pytest
import requests

class TestWeixin():
    _corpid="ww630f49269e06f865"
    _contact="YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"

    def setup(self):
        #获取通讯录的access_token
        url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._corpid}&corpsecret={self._contact}"
        r=requests.get(url=url)
        self.token=r.json()["access_token"]

    def test_wework_department(self):
        # 删除部门
        department_id=3
        url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        r=requests.get(url=url)
        print(r.json())


        #创建一个部门
        url=f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        create_data={
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
        }
        r=requests.post(url=url,json=create_data)
        print(r.json())

        # 获取整个部门的信息

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.get(url=url)
        print(r.json())

        # 更新部门
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        update_data={
            "id": 3,
            "name": "广州研发中心1"
        }
        r=requests.post(url=url,json=update_data)
        print(r.json())



    @pytest.mark.skip
    def test_wework_person(self):
        #获取某个成员的信息
        member="tong33"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={member}"
        r=requests.get(url=url)
        if r.json()["errcode"]==0:
            print(r.json())

        #删除一个成员
        user_id="tong33"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        r=requests.get(url=url)
        print(r.json())

        #创建一个成员
        create_data={
            "userid": "tong33",
            "name": "zeng1",
            "mobile": "13800000017",
            "department": [1, 2]

        }
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        r=requests.post(url=url,json=create_data)
        print(r.json())

        #更新一个成员的名字
        #企业微信的通讯录api需要改成编辑
        update_data={
            "userid": "tong33",
            "name": "zeng1111"
        }
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        r=requests.post(url=url,json=update_data)
        print(r.json())







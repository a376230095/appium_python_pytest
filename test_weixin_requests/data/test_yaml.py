from pprint import pprint

import yaml

from api.base_api import Base_api


def test_c():
    print(Base_api.template("tag_add.yml", {"token":"abc","tag_name":"haha"}))


def test_a():
    with open("tag_add.yml") as f:
        pprint(yaml.safe_load(f))

def test_b():
    with open("tag_test.yml","w") as f:
        token=1
        data = {
           "method": "post",
           "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
           "params": {"access_token": f"{token}"},
       }
        yaml.safe_dump(data,f)
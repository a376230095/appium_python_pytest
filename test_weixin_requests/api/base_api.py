from pprint import pprint
from string import Template
import requests
import json

import yaml
from jsonpath import jsonpath


class Base_api():
    def send(self,req:dict):
        # pprint(dict)
        r= requests.request(**req).json()
        # pprint(r)
        return r

    @classmethod
    def jsonpath(cls,json1,expr):
        return jsonpath(json1,expr)

    @classmethod
    def load(cls,path):
        with open(path,"r") as f:
            return yaml.safe_load(f)

    @classmethod
    def template(cls,path,dict1):
        with open(path,"r",encoding="UTF-8") as f:
            return yaml.safe_load(Template(f.read()).substitute(dict1))
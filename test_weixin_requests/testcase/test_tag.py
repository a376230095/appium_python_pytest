import json

import pytest
from api.base_api import Base_api
from api.tag import Tag



class TestTag(Base_api):
    _tag_data=Base_api.load("../data/tag_data.yml")
    @classmethod
    def setup_class(cls):
        cls.tag=Tag()

    def setup(self):
        pass

    @pytest.mark.parametrize(("old_name,new_name"),_tag_data)
    def test_all_tag(self,old_name,new_name):
        tag_data=self.tag.get()

        for tag_name in [old_name,new_name]:
            print(old_name,new_name)
            tag_id=self.jsonpath(tag_data,f"$..tag[?(@.name=='{tag_name}')].id")
            if tag_id:
                self.tag.delete(tag_id[0])

        assert self.tag.add(old_name)["errcode"] == 0
        tag_id = self.jsonpath(self.tag.get(), f"$..tag[?(@.name=='{old_name}')].id")[0]
        assert self.tag.update(tag_id,new_name)["errcode"] == 0



    def test_add_tag(self):
        print(Tag().add("abcde"))

    def test_get_tag(self):
        # print(json.dumps(self.tag.get(),indent=2)
        assert self.tag.get()["errcode"] == 0

    def test_delete(self):
        tag_name="abc"
        tag_data = self.tag.get()
        tag_id = self.jsonpath(tag_data, f"$..tag[?(@.name=='{tag_name}')].id")[0]
        print(Tag().delete(tag_id))

    def test_update(self):
        print(Tag().update("etMCs1DwAAsL96xN_6Y5gEfadl2qexbw","abcd"))


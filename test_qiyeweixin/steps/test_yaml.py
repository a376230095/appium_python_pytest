from typing import List, Dict

import yaml

"""
- by: XPATH
- locator: //*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]
- action: click
"""
def test_a():
    a:List[dict]=yaml.safe_load(open("main_steps.yml",encoding="utf-8"))
    for i in a:
        print(a)



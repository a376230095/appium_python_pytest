import json

def test_j():
    with open("a.json","w") as f:
        #创建一个json文件，用dump把python的数据类型转化成json格式的文件
        a={"a":[1,2,3],"b":True,"c":None,"d":False}
        json.dump(a,f)

    with open("a.json") as f:
        #打开json文件，用load把json格式文件转化成python的数据类型
        python_a=json.load(f)
        print(python_a)
        #dumps把python的数据类型转化成json格式
        json_a=json.dumps(python_a)
        print(json_a)
        #loads把json数据类型转化成python的数据类型
        python_b=json.loads(json_a)
        print(python_b)
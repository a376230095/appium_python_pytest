import yaml

with open("demo3.yml","w") as f:
    #dump接收python的数据类型，文件stream就是文件的f了
    yaml.dump({"a":[1,3]},stream=f)
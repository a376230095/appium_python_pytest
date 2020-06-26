import yaml

#转化成列表，-就是一个列表，yaml有严格的空格要求
print(yaml.load("""
 - a
 - b
 - c
 - d
"""))

#转化成字典
print(yaml.load("""
a: 1
"""))

#读取yaml的
print(yaml.load(open("demo.yml")))
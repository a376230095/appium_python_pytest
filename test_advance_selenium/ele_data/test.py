import yaml


def ele_data():
    with open("index",encoding="utf8") as f:
        data=yaml.safe_load(f)
        print(data)
ele_data()
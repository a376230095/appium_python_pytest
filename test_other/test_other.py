import yaml


def getdata():
    with open("./wework_data.yaml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


def test_a():
    print(getdata())
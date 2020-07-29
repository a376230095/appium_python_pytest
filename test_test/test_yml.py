import yaml


def test_v():
    with open("access_token.yml") as f:
        test=yaml.safe_load(f)
        print(test)
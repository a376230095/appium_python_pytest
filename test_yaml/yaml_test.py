import yaml
import pytest

with open("demo2.yml") as  f:
    a=yaml.safe_load(f)
    print(a)
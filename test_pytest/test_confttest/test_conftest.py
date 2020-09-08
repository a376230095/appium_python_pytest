import math

import pytest
class TestB():
    def test_a(self,login):
        print(math.pi)
        print("this is test_a")



    def test_b(self):
        print("this is test_a")


if __name__=="__main__":
    pytest.main(["-s","-v","test_conftest.py"])
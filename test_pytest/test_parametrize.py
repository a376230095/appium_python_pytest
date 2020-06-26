import yaml
import pytest

class TestP():
    #a和b是要传入的参数，通过yaml来导入列表的值进来，要一一对应
    @pytest.mark.parametrize(("a,b"),yaml.safe_load(open("test.yaml")))
    #函数要写上a和b两个变量
    def test_p(self,a,b):
        print(a,b)

    #后面的参数要用一个大括号括起来
    @pytest.mark.parametrize(("a,b,c,d"),(
                             [1,2,3,4],
                             [5,6,7,8],
                             [9,10,11,12]))
    def test_a(self,a,b,c,d):
        print(a,b,c,d)

    """
    #yaml的值
    -
      test: ccc
    """
    #由于参数化的值只能读取列表，所以yaml的顶层也得是列表，不然读取出来会有点问题
    @pytest.mark.parametrize("a",yaml.safe_load(open("dict.yaml")))
    def test_dict(self,a):
        print(a)




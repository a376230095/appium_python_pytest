import pytest

#fixture的优先级高于setup，而且如果有setup方法，会先运行fixture，再运行setup，再运行方法
@pytest.fixture()
def fixture():
    print("fixture function")

#每一个方法都会运行这个autouse的fixture，而且运行优先级高于普通的fixture
@pytest.fixture(autouse=True)
def auto_fixture():
    print("auto_fixture setup")
    #只要有yield，第一充当返回值的功能，第二是yield后面的步骤都是teardown
    yield 2
    print("auto_fixture teardown")


class TestFixture():
    def setup(self):
        print("setup function")

    def teardown(self):
        print("teardown function")

    #使用函数名为fixture的fixture方法
    def test_a(self,fixture):
        print("test a")

    #只要你要fixture的返回值的内容， 就必须穿fixture的函数名
    def test_b(self,auto_fixture):
        print("test b")
        print(auto_fixture)

    def test_c(self):
        print("test b")

if __name__=="__main__":
    pytest.main(["-v","-s","test_fixture.py"])
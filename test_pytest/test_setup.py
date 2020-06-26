import pytest

#方法第二优先级，只对外部的函数运行
def setup_function():
    print("setup_function function")

#倒数第二运行，只对外部的函数运行
def teardown_function(self):
    print("teardown function")

#在外的方法只会被function级别的运行，而且优先类的方法运行
def test_out_a():
    print("test_out_a")

#在外的方法只会被function级别的运行，而且优先类的方法运行
def test_out_b():
    print("test_out_a")

#当模块运行的时候，第一运行
def setup_module():
    print("setup_module fucntion")

#当模块结束的时候，倒数第一运行
def teardown_module(self):
    print("teardown_module function")

class TestA():

    #每个类的方法都运行，第4优先级
    def setup(self):
        print("setup function")

    #每个类只运行一次，第3优先级
    def setup_class(self):
        print("setup_class function")

    #每个类只运行一次，倒数第3优先级
    def teardown_class(self):
        print("teardown_class function")

    #每个类的方法都运行，倒数第4优先级
    def teardown(self):
        print("teardown function")

    #类的方法
    def test_inner_a(self):
        print("test_inner_a")

    #类的方法
    def test_inner_b(self):
        print("test_inner_b")

if __name__=="__main__":
    pytest.main(["-s","-v","test_setup.py"])
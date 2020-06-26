import pytest

class Testa():
    a=1
    #使用这个会忽略这条用例，pytest会显示出来被skip
    @pytest.mark.skip
    def test_a(self):
        print("test_a")

    #只有这条用例会被执行
    def test_b(self):
        print("test_b")

    #这个if是skip的条件，当a==1，才会被skip，这个用例被skip了
    @pytest.mark.skipif(a==1,reason="love you")
    def test_f(self):
        print("test_f")
        assert 1==1

    #这个if是skip的条件，当a==1，才会被skip，这个用例没有被skip
    @pytest.mark.skipif(a==2,reason="love you")
    def test_z(self):
        print("test_z")
        assert 1==2

    #xfail表示是xpass，因为用例是pass的，只是一个提示作用，在最后会被提示
    @pytest.mark.xfail
    def test_c(self):
        print("test_c")

    #xfail最后是fail，显示xfiailed，因为assert是False的，在最后会被提示
    @pytest.mark.xfail
    def test_d(self):
        print("test_d")
        assert False

if __name__=="__main__":
    #-r属性是打印出被skip的reason的原因
    pytest.main(["-v","-rs","test_skip_xfail.py"])
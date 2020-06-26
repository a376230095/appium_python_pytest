class Demo:

    def __init__(self, driver=None):
        print("init")
        self.driver = None
        driver=None
        print(self.driver)
        if driver is None:
            self.driver = 1
        else:
            self.driver = 2

class Demo2(Demo):
    def test1(self):
        return Demo3(self.driver)

class Demo3(Demo):
    def test(self):
        return self.driver

demo = Demo2()
print(demo.test1().test())
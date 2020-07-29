class Server():
    def __init__(self,CPU,memory,disk,operasystem):
        self.CPU=CPU
        self.memory=memory
        self.disk=disk
        self.__operasystem=operasystem

    def get_operasystem(self):
        return self.__operasystem


class Price(Server):
    def count_price(self):
        sum=round(self.CPU*1527.679+self.memory*100.21+self.disk*50.789,2)
        print(f"总价为{sum}元")


def test_a():
    a=Price(2,4,1000,"linux")
    a.count_price()


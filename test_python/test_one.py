"""
Persion类
属性：姓名，性别，年龄，存款金额
方法：吃，睡，跑，赚钱

FunnyMan类（喜剧演员）
继承父类Person的所有属性和方法
新增一个方法，fun()搞笑

SingerMan（歌手演员）
继承父类Person的所有属性和方法
覆写方法，赚钱，传参（monkey）
"""

class Person():
    name:str="default"
    gender:str="default"
    age:int =20
    __money:float=1000

    def __init__(self,name,gender,age,money):
        self.name=name
        self.gender=gender
        self.age=age
        self.__money=money

    def get_name(self):
        return self.__money

    def set_name(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eatting")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    def make_money(self):
        print(f"{self.name} could make money")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is funny")

class SingerMan(Person):
    def make_money(self,moneynum:str):
        print(f"{self.name} could make {moneynum} yuan")
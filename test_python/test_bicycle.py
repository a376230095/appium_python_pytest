"""
Bicycle类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入一个数字）

EBicycle（电动车）继承Bicycle，增加电池电量battery_level属性同构参数传入
1、full_charge(vol)，用来充电，vol为电量
2、run(km)方法用于骑行，每骑行10km消耗一度电，当用完电量调用Bicycle的run方法骑行

通过传入的骑行里程数，显示骑行结果（当电量耗尽，需要你真正骑的里程数）
"""
import yaml

class Bicycle():
    # 这是我实际需要手动骑行
    def run(self, km):
        print(f"还需要骑行骑行{km}km")

class EBicyle(Bicycle):
    # batter_level是当前的电量是多少，1度电可以消耗10km
    def __init__(self, battery_level):
        self.battery_level = battery_level

    # 这个方法其实很积累，没有实际充满电，因为battery_level没有达到最大，也没有限定battery_level的最大值
    def full_charge(self, vol):
        print(f"剩余电量为{vol}，已充满电量")

    # 这个方法已经是重写父类的run方法了
    def run(self, km):
        # 最大的电动骑行的公里数=电量*10km
        max_mile = self.battery_level * 10
        # km参数是指我一共需要骑行多少千里，剩余的可骑行的电动公里数就是km-最大可骑行公里数
        # 但如果km小于max_mile，肯定是一个负数，所以这个函数只能算一次了
        leave_mile = km - max_mile

        # 当剩余公里数是正数，表示电动骑行的续航不够
        if leave_mile > 0:
            # 肯定表示我骑行的max_mile
            print(f"已经使用电车骑行了{max_mile}km")
            # 由于父类的run已经被重写了，所以想要使用原来的run，就需要用到super()的方法去调用父类的run
            # leave_mile就表示需要手动骑行多少剩余的公里数
            super().run(leave_mile)
        else:
            # 如果leave_mile为负数，说明我的电动骑行续航够，只需要打印我实际骑行多少公里即可
            print(f"已经使用电车骑行了{km} km")

# 普通方式调用函数
# a=EBicyle(800)
# a.run(1000)

# 使用yaml数据来调用
with open("bicycle.yaml") as f:
    # 先导入yaml的文件，用data保存，这里是一个大的字典
    data = yaml.safe_load(f)

# 保存一个大的字典
mybicycle1 = data["mybicycle1"]
# 把要的参数都用变量保存好
my_battery = mybicycle1["battery_level"]
my_km = mybicycle1["km"]
# 直接使用变量就好了
a = EBicyle(my_battery)
a.run(my_km)

# 这里是为了使用yaml的引用功能
mybicycle1 = data["default"]
my_battery = mybicycle1["battery_level"]
my_km = mybicycle1["km"]
a = EBicyle(my_battery)
a.run(my_km)
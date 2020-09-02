import multiprocessing
# 拿到进程池
from multiprocessing import Pool
import os
import random
import time

# 定义一个进程的函数
def task(taskname):
    #统计进程运行的时间
    start_time=time.time()
    print(f"正在{taskname}")
    time.sleep(random.random())
    end_time=time.time()
    print(f"{taskname}运行结束")
    # return是给进程池的回调函数使用
    return f"{taskname}运行结束，用时：{end_time-start_time}，进程PID={os.getpid()}"

# 定义一个列表，接收所有进程的回调函数的return值
container=[]

# 定义回调函数，n就是接收return的值
def called(n):
    # 把return的值添加到container上
    container.append(n)

if __name__=="__main__":
    # 定义5个进程的线程池
    pool=Pool(5)
    # 定义7个进程
    tasks=["吃饭","睡觉","学习","打球","娱乐","看电视","不吃饭"]
    for t in tasks:
        # 使用异步非阻塞的线程池，添加回调函数
        pool.apply_async(task,args=(t,),callback=called)
    # 让进程池运行完之后再结束
    pool.close()
    # 一旦主进程结束，进程池也会结束，加入join，强制让进程池结束后，才运行主进程下面的代码
    pool.join()

    # 打印出回调函数的所有返回值
    for i in container:
        print(i)
    print("----over-----")


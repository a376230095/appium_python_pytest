import _thread
import logging
import threading
from time import sleep,ctime,time
logging.basicConfig(level=logging.DEBUG)

num=0
num1=1
lock=threading.Lock()
def loop(lk):
    start_time = time()
    global num
    lk.acquire()
    for i in range(30000000):
        num+=1
    print(f"num为：{num}")
    lk.release()
    end_time = time()
    print(f"用时{end_time - start_time},num的值为：{num}")
def loop1():
    global num1
    for i in range(30000000):
        num1+=1
    print(f"num为：{num}")


# def loop1(lk):
#     global num
#     lk.acquire()
#     for i in range(1000000):
#         num+=1
#     lk.release()

if __name__=="__main__":
    # start_time = time()
    # for i in range(2):
    #     t=threading.Thread(target=loop,args=(lock,))
    #     # t.setDaemon(False)
    #     t.start()
    # end_time = time()
    # print(f"用时{end_time - start_time},num的值为：{num}")
    start_time=time()
    loop1()
    loop1()
    end_time=time()
    print(f"用时{end_time-start_time},num的值为：{num1}")


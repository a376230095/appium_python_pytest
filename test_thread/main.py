import _thread
import logging
from time import sleep,ctime
#可以查看INFO的信息
logging.basicConfig(level=logging.INFO)

def loop0():
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

"""
#单纯一个main的进程，所以先等loop0执行了之后，才会去执行loop1，这样一共耗时6秒
def main():
    logging.info("start all at" + ctime())
    loop0()
    loop1()
    logging.info("end all at" + ctime())
"""
def main():
    #这里定义了两个线程，分别执行两个函数，由于sleep算是io操作吧，所以两个线程同步运行
    #时间就从原来的6秒变成了4秒
    #如果main不写sleep，等main结束了，两个线程都会结束，这是因为只要main线程结束了，就会强制结束内置的两个线程
    logging.info("start all at" + ctime())
    #这里添加一个线程，接收一个函数，没有参数就写()
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())
    sleep(6)
    logging.info("end all at" + ctime())

if __name__=="__main__":
    main()
import _thread
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.DEBUG)

loops=[2,4]
def loop(nloop,sec):
    logging.info(f"{nloop} start time：{ctime()}")
    sleep(sec)
    logging.info(f"{nloop} end time:{ctime()}")


def main():
    logging.info(f"main start time:{ctime()}")
    nloop=range(len(loops))
    threads=[]
    for i in nloop:
        thread=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(thread)
    for i in nloop:
        threads[i].start()
    #join需要在所以线程start之后才运行，这样才可以实现并发
    for i in nloop:
        threads[i].join()
    logging.info(f"main end time:{ctime()}")

if __name__=="__main__":
    main()

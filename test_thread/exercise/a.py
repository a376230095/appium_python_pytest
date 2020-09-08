import _thread
import logging
from time import sleep,ctime
logging.basicConfig(level=logging.DEBUG)

loops=[2,4]
def loop(nloop,sec,lock):
    logging.info(f"{nloop} start time：{ctime()}")
    sleep(sec)
    logging.info(f"{nloop} end time:{ctime()}")
    lock.release()


def main():
    logging.info(f"main start time:{ctime()}")
    locks=[]
    nloop=range(len(loops))
    for i in nloop:
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloop:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloop:
        while locks[i].locked():pass
    logging.info(f"main end time:{ctime()}")

if __name__=="__main__":
    main()

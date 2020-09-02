import threading
#死锁：线程A需要拿到线程B的锁，线程B也需要拿到线程A的锁，两者就傻掉了，一直等待，都等不到
import time

lock_a=threading.Lock()
lock_b=threading.Lock()
class Thread1(threading.Thread):
    def run(self):
        if lock_a.acquire():
            print(f"{self.name} 获取了a锁")
            time.sleep(0.1)
            if lock_b.acquire():
                print(f"{self.name} 获取了b锁")
                lock_b.release()
            lock_a.release()

class Thread2(threading.Thread):
    def run(self):
        if lock_b.acquire():
            print(f"{self.name} 获取了b锁")
            time.sleep(0.1)
            if lock_a.acquire():
                print(f"{self.name} 获取了a锁")
                lock_a.release()
            lock_b.release()


if __name__=="__main__":
    a=Thread1()
    b=Thread2()
    a.start()
    b.start()
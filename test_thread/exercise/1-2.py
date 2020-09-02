import threading
import time

def show():
    print(threading.current_thread().getName()+"子线程开启")
    time.sleep(3)
    print(threading.current_thread().getName()+"子线程结束")

print("主线程开启")
for i in range(3):
    t=threading.Thread(target=show)
    # 设置为True后，当主线程结束之后，程序结束，其他线程没有执行完毕也停止执行了，这个叫守护线程
    t.setDaemon(True)
    t.start()
print("主线程结束")


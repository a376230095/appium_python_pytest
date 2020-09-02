import threading
import time


def show(mes):
    print("子线程开启")
    time.sleep(3)
    print(f"程序正在执行{mes}次")
    print("子线程结束")

print("主线程开启")
t = threading.Thread(target=show, args=(1,))
# 通常主线程和子线程是分开的，所以当主线程执行完毕之后，由于子线程还没执行完毕，子线程在主线程后执行完毕
t.start()
# 加入join之后，主线程会等子线程执行完毕之后，才会执行join后面的操作
# join需要在start前面执行
t.join()
print("主线程结束")


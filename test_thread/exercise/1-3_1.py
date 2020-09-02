import threading
import time
# 项目背景：创建2个线程，同时共享number数据，都加到1百万，理论上两个线程执行完毕后，就获取200w，但最终只有140多w
number=0

def count():
    global number
    for i in range(1000000):
        number+=1
    # Thread-1子线程的number=1264209
    # Thread-2子线程的number=1464677
    print(threading.current_thread().getName()+f"子线程的number={number}")

print("主线程开始")

for i in range(2):
    t=threading.Thread(target=count,)
    t.start()

time.sleep(0.3)
print("主线程结束")
# 最终的number=1464677
print(f"最终的number={number}")

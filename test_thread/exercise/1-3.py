import threading
import time

number=0
# 创建一个互斥锁
lock=threading.Lock()

def count(lk):
    global number
    # 这里加锁，加锁之后，要等该线程执行完毕后，才会去执行其他线程，所以不会出现问题
    lk.acquire()
    for i in range(1000000):
        if number!=i:
            print(f"当前线程是：{threading.current_thread().getName()},number={number},i={i}")
        number+=1
    print(threading.current_thread().getName()+f"子线程的number={number}")
    # 程序完成后才解锁
    lk.release()

print("主线程开始")


for i in range(2):
    t=threading.Thread(target=count,args=(lock,))
    t.start()
    # 加了join()虽然可以达到目的，但是整个程序是串行执行，并没有并行执行
    # 因为join之后，程序不会去执行下一个线程
    # t.join()

time.sleep(0.3)
print("主线程结束")
print(f"最终的number={number}")

# 这里是加锁，通过with的方式去加
# def countwith(lk):
#     global number
#     # 和lk.acquire()、lk.release()的作用等价
#     with lk:
#         for i in range(1000000):
#             number+=1
#         print(threading.current_thread().getName()+f"子线程的number={number}")
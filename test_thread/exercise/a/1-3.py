import threading
import time

number=0
# 创建一个互斥锁
lock=threading.Lock()

def count(lk):
    global number
    # 这里加锁
    lk.acquire()
    for i in range(1000000):
        number+=1
    print(threading.current_thread().getName()+f"子线程的number={number}")
    # 程序完成后才解锁
    lk.release()

def countwith(lk):
    global number
    # 和lk.acquire()、lk.release()的作用等价
    with lk:
        for i in range(1000000):
            number+=1
        print(threading.current_thread().getName()+f"子线程的number={number}")


print("主线程开始")
# 程序目的是获得2000000，但实际只有1400000左右，是因为cpu并不是并行执行两个线程，是先执行线程1，然后执行线程2，然后再执行线程1，交替执行
# 当我们以为两个线程都会共享number，其实并没有共享number，导致number在两个线程的不是同一个内存的地址

for i in range(2):
    t=threading.Thread(target=countwith,args=(lock,))
    t.start()
    # 加了join()虽然可以达到目的，但是整个程序是串行执行，并没有并行执行
    # 因为join之后，程序不会去执行下一个线程
    # t.join()

time.sleep(0.3)
print("主线程结束")
print(f"最终的number={number}")
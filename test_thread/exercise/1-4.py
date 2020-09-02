# 导入多进程
import multiprocessing
import time
import os

def sing(a):
    # os.getpid()是打印当前进程的PID
    print(f"子进程pid={os.getpid()}")
    for i in range(3):
        print(f"我在唱歌:歌名是{a}")
        time.sleep(0.5)

def dance(b):
    print(f"子进程pid={os.getpid()}")
    for i in range(3):
        print(f"我在跳舞，和{b}跳舞")
        time.sleep(0.3)

if __name__=="__main__":
    # os.getppid()获取父进程的PID
    print(f"父进程的pid={os.getppid()}")
    a="a"
    b="b"
    # 创建进程，target指向要执行的函数，args传元祖，传函数的参数
    pro_sing=multiprocessing.Process(target=sing,args=(a,))
    pro_dance=multiprocessing.Process(target=dance,args=(b,))
    # 开始运行进程
    pro_dance.start()
    pro_sing.start()
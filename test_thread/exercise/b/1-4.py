import multiprocessing
import time
import os

def sing(a):
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
    print(f"父进程的pid={os.getppid()}")
    a="a"
    b="b"
    pro_sing=multiprocessing.Process(target=sing,args=(a,))
    pro_dance=multiprocessing.Process(target=dance,args=(b,))
    pro_dance.start()
    pro_sing.start()
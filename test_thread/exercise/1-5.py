import os
import shutil
import multiprocessing
import threading
target_dir="b"
source_dir="a"


if not os.path.exists("b"):
    os.mkdir("b")

#
all_file_path=os.listdir(source_dir)
all_file_path=[os.getcwd()+"\\"+i for i in all_file_path]
def copy(source_dir,targetdir):
    shutil.copy(source_dir,targetdir)

print("start")
for i in all_file_path:
    t=threading.Thread(target=copy,args=(i,target_dir))
    t.start()

print("end")
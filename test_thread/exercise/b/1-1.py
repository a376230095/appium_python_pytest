import threading
import subprocess
import time


def get_adb_logcat():
    a=subprocess.Popen("adb logcat -v time",stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    with open("adb_logcat.txt","w") as f:
        for i in a.stdout:
            f.writelines(str(i).lstrip(r"b'").rstrip(r"\r\r\n'")+"\n")


t=threading.Thread(target=get_adb_logcat)
t.setDaemon(True)
t.start()
time.sleep(2)

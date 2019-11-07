#!/usr/bin/python3

import threading
import time

exitFlag = 0
#global value


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        global exitFlag
        while not exitFlag:
            print(time.ctime(time.time()))
            time.sleep(1)


def fun1():
    global exitFlag
    for i in range(10):
        print("fun1 is running exitFlag: ", exitFlag)
        time.sleep(1)
    
    exitFlag = 1
    print(exitFlag)


thread1 = myThread(1, "thread 1", 1)
thread1.start()
thread2 = threading.Thread(target=fun1)
thread2.start()
thread1.join()
print("thread 1 off")

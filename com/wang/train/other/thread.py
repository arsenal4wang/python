# coding=utf8
import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print "%s: %d" % ( threadName, count )

# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2, ))
    thread.start_new_thread(print_time, ("Thread-2", 4, ))
    thread.start_new_thread(print_time, ("Thread-3", 4, ))
except:
    print "Error: unable to start thread"

while 1:
    pass

print printTime("we", "100000")
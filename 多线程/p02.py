'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread

def loop1():
    print('Start loop 1 at:', time.ctime())
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2():
    print('start:', time.ctime())
    time.sleep(2)
    print('End:', time.ctime())


def main():
    print('Start at:', time.ctime())
    _thread.start_new_thread(loop1,())
    _thread.start_new_thread(loop2,())
    print('all End', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
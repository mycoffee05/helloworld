# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：code以文件形式存入一个文档
- 进程：程序运行的一个状态 pid
    - 包含地址空间，内存，数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程：
    - 一个进程的独立运行片段，一个进程可以由多个线程共同运行
    - 轻量化的进程
    - 一个进程的多个线程共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
- Python包
    - thread:有问题，不好用，python3改成了_thread
    - threading:通行的包
    - p01,p02
    - p03:多线程，传参数
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
        4. p04
        5. p05:join后跟p04比较
        - 守护线程-daemon 
            - 随时可以kill 同主线程同时消失
            - 如果在程序中将子线程设置为守护线程，则子线程会在主线程结束时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程运行
            - 守护线程案例能否有效果跟环境相关
            - p06 非守护线程
            - p07 守护线程 必须在子线程start之前设置
        - 线程常用属性
            - threading.currentThread：返回当前线程变量
            - threading.enumerate:返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的状态
            - threading.activeCount: 返回正在运行的线程数量，效果跟 len(threading.enumerate)相同
            - thr.setName: 给线程设置名字
            - thr.getName: 得到线程的名字
    - 直接继承自threading.Thread
        - 直接继承Thread
        - 重新run函数
        - 类实例直接运行
        - p09
        - p10 工业风案例
        
- 共享变量 
    - 共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题    
    - p11
    - 锁(lock):
        - 是一个标准，表示一个线程在占用一些资源 
        - 使用方法：
            - lock.acquire()上锁
            - 使用共享资源 
            - lock.release()解锁
        - 案例p12
        - 锁谁：哪个资源需要多个线程共享，锁哪个
        - 令牌：谁有令牌，谁有资格谁能访问资源
    - 线程安全问题
        - 如果一个资源/变量，他对于多线程来讲，不枷锁也不会引起问题，则称为线程安全
        - 线程不安全变量类型：list,set,dict
        - 安全变量类型：queue,
# 共享变量的问题
    - 生产者消费者模型
    - 搭建消息队列 案例p13
    - queue是一个用来存放变量的数据结构，特点是先进先出
    - 死锁问题，p14
    - 锁的等待时间问题，p15
    - semphore 006
        - 允许一个资源最多有几个多线程同时使用
        - p16
    - threading.Timer p17
        - Timer是利用多线程，在指定时间后启动一个功能
    - 可重入锁                     
        - 一个锁可以被一个线程多次申请
        - 解决递归调用的时候，需要申请锁的情况 p18
    
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 派生进程的主要替代方案
- multiprocessing
    - 使用threading接口派生，使用子进程
    - 允许为多核或者多cpu派生进程，接口跟threading 非常相似
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
# 多进程
    - 进程间通讯（InterprocessCommunication,IPC）
    - 进程之间没有任何共享状态
    - 进程的创建 p19 直接生成进程的实例对象
    - 派生 p20     
- 在os中查看pid和ppid以及他们的关系
    - 案例21 
- 生产者消费者模型
    - JoinableQueue    p22
    - 哨兵的使用，p23
    - 哨兵的改进 p24      
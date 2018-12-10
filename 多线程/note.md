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
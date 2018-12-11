# 协程
- 参考资料
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    - https://segmentfault.com/a/1190000009781688
# 迭代器
- 可迭代（Iterable）：直接作用于for循环的变量
- 迭代器（Iterator）：一定是可迭代的，可以用于for循环，还可以被next调用
- list是典型的迭代对象，但不是迭代器
- isinstance判断某个变量是不是一个实例 p02
- 可通过iter函数进行可迭代对象和迭代器之间的转换 p03
# 生成器
- generator:一边循环一边计算下一个元素的机制/算法
- 满足三个条件：、
    - 每次调用都生产出for循环需要的下一个元素
    - 如果达到最后一个后，报出StopIteration异常
    - 可以被next函数调用
- 如何生成一个生成器
    - 直接使用 p04
    - 如果函数中包含yield,则这个函数就叫做生成器
    - next调用函数，遇到yield返回     p05
    - for循环调用 p06
    
# 协程
- 历史历程
- 3.4引入协程，用yield实现
- 3.5引入协程语法
- 实现的协程比较好的包有asyncio, tornado, gevent
- 定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序”。
- 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程的返回
    - yield 返回
    - send 调用 
    - p07
- 协程的四个状态
    - inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime)
    - 代码案例p08
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给next函数或者send方法的调用方（即触发协程的对象）
    - 终止协程方式：发送某个哨符值，让协程推出，内置None和Ellipsis等常量
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象value属性保存返回值
    - yield from通道，从内部捕获StopIteration异常 
    - p09   
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式出暂停，调用方可以直接吧数据发给子生成器
        - 子生成器再把产出的值发给调用方
        - 子生成器会在解释器会抛出StopIteration，并且把返回值附加到异常对象上  
        - p10
        
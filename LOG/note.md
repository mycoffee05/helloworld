# 2.1 logging模块的处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个接口
    - 处理器（Handler）：把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细的控制日志输出
    - 格式器（formatter）：对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
        
                Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
                Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
                Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象
                Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()	创建一个与它们的方法名对应等级的日志记录
                Logger.exception()	创建一个类似于Logger.error()的日志消息
                Logger.log()	需要获取一个明确的日志level参数来创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()            
- Handler 
    -  把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter
    - 不需要直接使用，Handler是基类
        - Handler.setLevel()	设置handler将会处理的日志消息的最低严重级别
        - Handler.setFormatter()	为handler设置一个格式器对象
        - Handler.addFilter() 和 Handler.removeFilter()	为handler添加 和 删除一个过滤器对象
        - logging.StreamHandler	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
        - logging.FileHandler	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
        - logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按大小切割
        - logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
        - logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
        - logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
        - logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。
- Formater类
    - 直接实例化
    - 科技继承Format添加特定内容
    - 三个参数
        - fmt
        - datefmt
        - style
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息具体内容
    - 案例02    
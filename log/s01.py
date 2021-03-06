import logging

LOG_FORMAT = '%(asctime)s=====%(levelname)s======%(message)s' #格式设置
logging.basicConfig(filename='shang.log',level=logging.DEBUG,format=LOG_FORMAT) #左ctrl点函数 直接help

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
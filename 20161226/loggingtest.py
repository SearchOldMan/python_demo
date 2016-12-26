#coding=utf-8
import logging
#基本设置
logging.basicConfig(level=logging.INFO,filename="myloggingconfig.log")
logging.info("start program")
logging.info("trying to divide 1 by 0")
try:
    print 1/0
except Exception,e:
    logging.error(e)
logging.info("the division success")
logging.info("end program")
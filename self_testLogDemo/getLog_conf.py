"""
@author:赵公子
@date:2022/7/20 23:19
@filename:getLog_conf.py
"""
import logging
import logging.config

logging.config.fileConfig("logging.conf")

root_logger = logging.getLogger()
root_logger.debug("这是配置文件读取root记录器日志信息")

applog_logger = logging.getLogger("applog")
applog_logger.info("这是配置文件读取applog记录器日志信息")

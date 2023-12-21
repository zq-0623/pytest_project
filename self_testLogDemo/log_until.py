"""
@author:赵公子
@date:2022/7/19 23:08
@filename:log_until.py
"""
import logging

from logging.handlers import TimedRotatingFileHandler

# 创建日志对象
logger = logging.getLogger("zhao")
# 设置日志显示级别
logger.setLevel(logging.DEBUG)

# 添加控制台，用于输出日志到控制台
console_handler = logging.StreamHandler()
# 设置控制台输出日志级别
console_handler.setLevel(logging.DEBUG)

# 添加日志文件，用于输出日志文件
file_handler = logging.FileHandler("./test.log", mode="w", encoding="utf-8")
# 设置文件输出日志级别
file_handler.setLevel(logging.INFO)

# 将handler添加至日志器中
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 自定义日志格式
console_formatter = logging.Formatter("%(name)s--->%(asctime)s--->%(levelname)8s--->%(message)s")
file_formatter = logging.Formatter("%(asctime)s--->%(levelname)8s--->%(message)s")

# 将日志格式赋予日志器handler
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# 定义一个过滤器
flt = logging.Filter("zhao")
# 关联过滤器
# logger.addFilter(flt)
file_handler.addFilter(flt)

# 输出不同级别的日志
logger.debug("===========调试信息=============")
logger.info("===========正常信息=============")
logger.warning("===========警告信息=============")
logger.error("===========错误信息=============")
logger.critical("===========严重信息=============")

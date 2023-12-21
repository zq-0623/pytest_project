# -*- coding: utf-8 -*-
"""
@author:赵公子
@date:2022/7/22 23:39
@filename:logger.py
"""
import logging
import os
import time

# 获取项目相对路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(BASE_PATH)  # D:\ProjectDemo\PythonProject\pytest_project
# print(os.path.dirname(os.path.realpath(__file__)))  # D:\ProjectDemo\PythonProject\pytest_project\common
# print(__file__)  # D:\ProjectDemo\PythonProject\pytest_project\common\logger.py
# 创建日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
# print(LOG_PATH)
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    def __init__(self):
        # 创建以年月日为日志文件名
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))

        # 创建日志对象
        self.logger = logging.getLogger()
        # 设置日志显示级别
        self.logger.setLevel(logging.DEBUG)

        # 添加控制台，用于输出日志到控制台
        self.console_handler = logging.StreamHandler()
        # 设置控制台输出日志级别
        self.console_handler.setLevel(logging.DEBUG)

        # 添加日志文件，用于输出日志文件
        self.file_handler = logging.FileHandler(self.logname, "a", encoding="utf-8")
        # 设置文件输出日志级别
        self.file_handler.setLevel(logging.DEBUG)

        # 将handler添加至日志器中
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)

        # 自定义日志显示格式
        self.formatter = logging.Formatter(
            '%(asctime)s  %(filename)s %(lineno)d  %(levelname)s : %(message)s'
        )

        # 将自定义日志格式赋予日志器handler
        self.console_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)


logger = Logger().logger

# if __name__ == '__main__':
#     logger.debug("=====开始测试=====")
#     logger.debug(BASE_PATH)
#     logger.debug(LOG_PATH)
#     logger.debug("=====结束测试=====")


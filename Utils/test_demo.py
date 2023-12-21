# -*- coding: utf-8 -*-
"""
@author:赵公子
@date:2022/7/22 23:13
@filename:test_demo.py
"""
import logging, time, os

import pytest

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "self_testLogDemo")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger
if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.info(BASE_PATH)
    logger.info(LOG_PATH)
    logger.debug("---测试结束---")



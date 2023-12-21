# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 22:34
@Auth ： ZhaoQiang
@File ：getdictLog_conf.py
@IDE ：PyCharm
"""
import logging.config
from common import settings

logging.config.dictConfig(settings.LOGGINGDIC)
logger1 = logging.getLogger("用户充值")
logger1.info("字典配置用户充值！")

logger2 = logging.getLogger("用户操作")
logger2.info("字典配置用户充值！")

logger3 = logging.getLogger("用户转账")
logger3.info("字典配置用户充值！")

logger4 = logging.getLogger("用户体现")
logger4.info("字典配置用户充值！")


# 日志轮转

# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/31 22:48
@Auth ： zhaoqiang
@File ：Api_method.py
@IDE ：PyCharm
"""
import requests
from common.logger import logger


class ApiRequest:
    def __init__(self):
        self.session = requests.session()

    def method(self, method, url, data=None, params=None, json=None, headers=None, **kwargs):
        logger.info("请求方式：%s" % method)
        return self.session.request(method, url, data=data, params=params, json=json, headers=headers, **kwargs)

    def close_session(self):
        self.session.close()


req = ApiRequest()

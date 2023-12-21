# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/31 22:50
@Auth ： zhaoqiang
@File ：DMI_Case.py
@IDE ：PyCharm
"""
from common.Api_method import req
from common.logger import logger
from Utils.util_tools import Utils
import pytest


class Test_DMI:
    @pytest.mark.smoke
    def test_DMI(self):
        url = "http://114.80.155.47:22013/v2/newsinteractive"
        headers = {
            "token": "MitakeWeb",
            "symbol": "000530.sz",
            "src": "d",
            "param": "0, 20"
        }
        DMI = req.method("GET", url=url, headers=headers)
        logger.info("请求接口为===》{}".format(url))
        logger.info("请求参数代码为===》{}".format(headers.get("symbol")))
        DMI_content = DMI.json()["List"]
        INTERACTIVEID_list = []
        for i in range(len(DMI_content)):
            for key, values in DMI_content[i].items():
                if key == "INTERACTIVEID":
                    INTERACTIVEID_list.append(values)
        result = Utils().list_is_unique(INTERACTIVEID_list)
        logger.info("列表中不存在重复元素：====》{}".format(result))
        req.close_session()


# testdmi = Test_DMI()
# testdmi.test_DMI()



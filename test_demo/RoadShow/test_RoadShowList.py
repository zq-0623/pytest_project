# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/1 21:58
@Auth ： ZhaoQiang
@File ：test_RoadShowList.py
@IDE ：PyCharm
"""
import os

from Utils.read_data import ReadFileData
from common.Api_method import ApiRequest
from common import settings,host
import logging.config
import random
import pytest

# 忽略https警告
import urllib3
urllib3.disable_warnings()

logging.config.dictConfig(settings.LOGGINGDIC)
logger = logging.getLogger()


# print(os.path.dirname(os.path.dirname(__file__)))

class TestRoadShow:
    req = ApiRequest()
    # logger = Logger().logger
    # subtype = ["_2","_3","_4","_5","_7","_8","_11","_13","_14","_15","_20","_21","_22","_23","_25","_26"]
    # subtype = ["_2"]
    subtype = "_2"
    logger.info("==========获取路演列表接口开始测试==========")

    # 获取路演ID
    # pytest框架忽略https警告
    @pytest.mark.filterwarnings("ignore::UserWarning")
    @pytest.mark.smoke
    def test_get_RoadShowListId(self):
        yaml_data = ReadFileData.read_yaml(self,"./testcase.yaml")
        # url2 = yaml_data[0]["ip"]
        # host = yaml_data[1]["url"]
        # self.logger.info("==========获取路演列表接口开始测试==========")
        # url = yaml_data[0]["ip"] + yaml_data[1]["url"]
        url = host + yaml_data[1]["url"]
        headers = {
            "token": yaml_data[0]["token"],
            "param": yaml_data[2]["param"],
            "symbol": yaml_data[2]["symbol"]
        }
        response = self.req.method(yaml_data[1]["method"], url=url, headers=headers, verify=False)
        logger.info("请求接口为===》{}".format(url))
        logger.info("请求参数代码为===》{}".format(headers.get("symbol")))
        RoadShowList = response.json()["roadshows"]
        ID_list = []
        for i in range(len(RoadShowList)):
            if RoadShowList[i]["askStatus"] == 1 and RoadShowList[i]["status"] != "已结束":
                ID = RoadShowList[i]["id"]
                # self.logger.info(ID)
                ID_list.append(ID)
        logger.info(ID_list)
        return ID_list
        # self.logger.info("==========获取路演列表接口结束测试==========")

    # 获取嘉宾ID
    @pytest.mark.filterwarnings("ignore::UserWarning")
    @pytest.mark.smoke
    def test_get_GuestList(self):
        logger.info("==========获取嘉宾列表接口开始测试==========")
        url = "https://yunxjqly.sseinfo.com/m_public/getGuestListByRsid.do"
        params = {
            "rsId": random.choice(TestRoadShow.test_get_RoadShowListId(self)),
            "isShowOwn": 1
        }
        headers = {
            "token": "MitakeWeb",
            "symbol": "getrs"
        }
        response = self.req.method("GET", url=url, params=params, headers=headers, verify=False, timeout=7)
        logger.info("请求接口为===》{}".format(url))
        logger.info("请求路演ID为===》{}".format(params.get("rsId")))
        GuestList = response.json()["guestList"]
        if GuestList is None:
            print("嘉宾列表为空的路演ID为".format(params.get("rsId")))
        uid_list = []
        for i in range(len(GuestList)):
            uid = GuestList[i]["uid"]
            uid_list.append(uid)
        print(uid_list)
        return uid_list
        # self.logger.info("==========获取嘉宾列表接口结束测试==========")

    # 路演提问接口
    @pytest.mark.filterwarnings("ignore::UserWarning")
    @pytest.mark.smoke
    def test_askToGuest(self):
        logger.info("==========路演提问接口开始测试==========")
        url = "https://yunxjqly.sseinfo.com:22011/v1/askToGuest"
        headers = {"token": "MitakeWeb"}
        data = {
            "rsId": random.choice(TestRoadShow.test_get_RoadShowListId(self)),
            "guestId": random.choice(TestRoadShow.test_get_GuestList(self)),
            "content": "ggggg",
            "userId": "gg",
            "nickName": ""
        }
        response = self.req.method("POST", url=url, headers=headers, json=data, verify=False, timeout=7)
        logger.info("请求接口为===》{}".format(url))
        logger.info("请求路演ID为===》{}".format(data.get("rsId")))
        logger.info("请求嘉宾ID为===》{}".format(data.get("guestId")))
        print(response.text)

        logger.info("==========路演提问接口结束测试==========")


if __name__ == '__main__':

    for server in host.SERVERS:
        if server["use"] == 1:
            host = server["ip"]
            env = server["env"]
            # 分离ip和端口
            ip = server["ip"].split(":")[1].replace("/","")
            port = server["ip"].split(":")[2].replace("/","")

            content = {
                "host": host,
                "env": env
            }
test = TestRoadShow()
test.test_get_RoadShowListId()
# test.test_get_GuestList()

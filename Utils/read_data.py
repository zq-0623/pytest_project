# -*- coding: utf-8 -*-
"""
@author:赵公子
@date:2022/7/23 23:14
@filename:read_data.py
"""

from common.logger import Logger
import os
import yaml
import json
from configparser import ConfigParser
from Utils.util_tools import Utils

print(os.path.abspath(os.getcwd().split("Utils")[0]))

#
# path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# # print(path)
# yaml_path = os.path.join(path, "test_data")
# # print(yaml_path)
# yaml_name = r"\data.yaml"
# log_yamlPath = yaml_path + yaml_name
logger = Logger().logger


# def read_yaml(log_yamlPath):
#     logger.info("加载{}文件".format(log_yamlPath))
#     with open(log_yamlPath, encoding="utf-8") as file:
#         yaml_content = yaml.load(stream=file, Loader=yaml.FullLoader)
#         logger.info("加载到{}文件".format(log_yamlPath))
#         for value in yaml_content:
#             logger.info("读取到{}文件中的{}内容".format(log_yamlPath, value["account"]))
#             logger.info("读取到{}文件中的{}内容".format(log_yamlPath, value["password"]))
#
#
# def read_yamls(log_yamlPath):
#     logger.info("加载{}文件".format(log_yamlPath))
#     with open(log_yamlPath, encoding="utf-8") as file1:
#         yamls_content = yaml.load_all(stream=file1, Loader=yaml.FullLoader)
#         logger.info("加载到{}文件".format(log_yamlPath))
#         for values in yamls_content:
#             logger.info("读取到{}文件中的内容:{}".format(yaml_name, values))
#
#
# try:
#     # read_yaml(log_yamlPath)
#     read_yamls(log_yamlPath)
# except Exception as e:
#     logger.error(e)


# 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData:

    def __init__(self):
        pass

    def read_yaml(self, file_path):
        """
        :param file_path:
        :return: 加载到的数据
        """
        logger.info("加载{}文件......".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        logger.info("读到数据===>>{}".format(data))
        return data

    def read_json(self, file_path):
        """
        :param file_path:
        :return: 加载到的数据
        """
        logger.info("加载{}文件......".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        logger.info("读到数据===>>{}".format(data))
        return data

    def read_ini(self, file_path):
        """
        :param file_path:
        :return: 加载到的数据
        """
        logger.info("加载{}文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="utf-8")
        data = dict(config._sections)
        print(data)
        return data

    def read_config_yaml(self, base_url):
        with open(Utils().get_object_path() + "config.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data[base_url]
            # print(data[base_url])

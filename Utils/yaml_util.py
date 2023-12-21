# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/12 23:24
@Auth ： ZhaoQiang
@File ：yaml_util.py
@IDE ：PyCharm
"""
import os

import yaml


# 写入
def write_yaml(data):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取
def read_yaml():
    with open(os.getcwd() + r"/extract.yaml", encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


# 清空
def clean_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()



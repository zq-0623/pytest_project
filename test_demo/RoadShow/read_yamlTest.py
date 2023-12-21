# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/6 22:05
@Auth ： ZhaoQiang
@File ：read_yamlTest.py
@IDE ：PyCharm
"""

from Utils import read_data



def read_yaml():
    url = read_data.ReadFileData.read_yaml("./testcase.yaml")
    print(url)

read_yaml()


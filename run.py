# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/15 22:57
@Auth ： ZhaoQiang
@File ：run.py
@IDE ：PyCharm
"""
import pytest
import time,os
import requests
from Utils.yaml_util import write_yaml,read_yaml,clean_yaml

if __name__ == '__main__':
    pytest.main()
    # time.sleep(3)
    # os.system("allure generate ./temps -o ./reports --clean")
    write_yaml({"name":"zhaogongzi"})
    print(read_yaml())
    clean_yaml()
    clean_yaml()
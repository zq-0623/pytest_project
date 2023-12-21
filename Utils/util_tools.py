# -*- coding: utf-8 -*-
"""
@author:Qiang.zhao
@date:2022年07月06日 23:46:23
@file:util_tools.py
@IDE:PyCharm
@project_name:pytest_project
"""
import os


class Utils:

    def list_is_unique(self, lst):
        return len(lst) == len(set(lst))

    # 获取项目根目录
    def get_object_path(self):
        return os.path.abspath(os.getcwd().split("Utils")[0])

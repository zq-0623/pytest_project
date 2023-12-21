# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/20 22:51
@Auth ： ZhaoQiang
@File ：parameterize_util.py
@IDE ：PyCharm
"""

import json
import yaml
# 读取测试用例yaml文件
from Utils.read_data import ReadFileData
from Utils.util_tools import Utils


# def read_testcase_yaml(yaml_path):
#     with open(Utils().get_object_path() + yaml_path, 'r', encoding='utf-8') as f:
#         caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
#         # 单纯复制修改参数的模式
#         if len(caseinfo) >= 2:
#             return caseinfo
#         else:  # 有数据驱动的场合
#             if "parameterize" in dict(*caseinfo).keys():
#                 new_caseinfo = ddt(*caseinfo)
#                 return new_caseinfo
#             else:
#                 return caseinfo
#
#
# def ddt(caseinfo):
#     if "parameterize" in caseinfo.keys():
#         caseinfo_str = json.dumps(caseinfo)
#         for param_key, param_value in caseinfo["parameterize"].items():
#             key_list = param_key.split("-")
#             print("------key和value------")
#             print(key_list,param_value)
#             length_flag = True
#             print("------data数据列表------")
#             # 规范yaml数据文件的写法
#             data_list = ReadFileData().read_yaml(param_value)
#             print(data_list)
#             for data in data_list:
#                 if len(data) != len(key_list):
#                     length_flag = False
#                     break
#             # 替换值
#             print("------替换值------")
#             new_caseinfo = []
#             if length_flag:
#                 for x in range(1, len(data_list)):  # 循环数据的行数
#                     temp_caseinfo = caseinfo_str
#                     for y in range(0, len(data_list[x])):  # 循环数据列
#                         if data_list[0][y] in key_list:
#                             # 替换原始的yaml里面的$ddt{}
#                             # 数字类型去掉“”
#                             if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
#                                 temp_caseinfo = temp_caseinfo.replace('"$ddt{'+data_list[0][y]+'}"',str(data_list[x][y]))
#                             else:
#                                 temp_caseinfo = temp_caseinfo.replace("$ddt{"+data_list[0][y]+"}", str(data_list[x][y]))
#                     print(temp_caseinfo)
#
#                     new_caseinfo.append(json.loads(temp_caseinfo))
#             return new_caseinfo
#     else:
#         return caseinfo


# 定义read_testcase_yaml函数，参数为yaml_path
def read_testcase_yaml(yaml_path):
    # 打开yaml文件
    with open(Utils().get_object_path() + yaml_path, 'r', encoding='utf-8') as f:
        # 读取yaml文件并解析为dict格式
        caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
        # 如果yaml文件只有1个dict，直接返回
        if len(caseinfo) >= 2:
            return caseinfo
        else:  # 如果有数据驱动的场合
            # 判断caseinfo中是否含有"parameterize"键
            if "parameterize" in dict(*caseinfo).keys():
                # 对caseinfo进行数据驱动处理
                new_caseinfo = ddt(*caseinfo)
                return new_caseinfo
            else:
                return caseinfo


# 定义ddt函数，参数为caseinfo
def ddt(caseinfo):
    if "parameterize" in caseinfo.keys():  # 判断caseinfo中是否含有"parameterize"键
        # 将caseinfo转为字符串格式
        caseinfo_str = json.dumps(caseinfo)
        for param_key, param_value in caseinfo["parameterize"].items():
            # 将param_key按"-"切分成列表
            key_list = param_key.split("-")
            print("------key和value------")
            print(key_list, param_value)
            length_flag = True  # 初始化长度标记为True
            print("------data数据列表------")
            # 用ReadFileData().read_yaml读取param_value所对应的yaml文件并存入data_list
            data_list = ReadFileData().read_yaml(param_value)
            print(data_list)
            for data in data_list:  # 遍历data_list
                if len(data) != len(key_list):  # 如果元素长度与key_list长度不相等，将长度标记设为False并跳出循环
                    length_flag = False
                    break
            print("------替换值------")
            new_caseinfo = []  # 定义新的caseinfo列表
            if length_flag:  # 如果长度标记为True
                for x in range(1, len(data_list)):  # 循环数据的行数
                    temp_caseinfo = caseinfo_str  # 将caseinfo_str赋值给temp_caseinfo
                    for y in range(0, len(data_list[x])):  # 循环数据列
                        if data_list[0][y] in key_list:  # 如果data_list的首行元素在key_list中
                            # 将原始的yaml里面的$ddt{}替换成对应的值
                            # 如果是数字类型，去掉双引号
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                      str(data_list[x][y]))
                            else:
                                temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                      str(data_list[x][y]))
                    print(temp_caseinfo)

                    # 将temp_caseinfo转为json格式并添加到新的caseinfo列表中
                    new_caseinfo.append(json.loads(temp_caseinfo))
            return new_caseinfo
    else:
        return caseinfo  # 如果caseinfo中没有"parameterize"键，直接返回原来的caseinfo列表


ddt(ReadFileData().read_yaml("../testcase/DmiWenDa/dmi_testcase.yaml"))

# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/14 23:02
@Auth ： ZhaoQiang
@File ：demo.py
@IDE ：PyCharm
"""
import json

import pytest
import yaml
from contextlib import ExitStack
from Utils.read_data import ReadFileData


def read_yaml(yaml_path):
    """
    :param yaml_path:
    :return: 加载到的数据
    """
    # Logger().logger.info("加载{}文件......".format(file_path))
    with open(yaml_path, encoding="utf-8") as f:
        caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
        if len(caseinfo) >= 2:
            return caseinfo

        else:
            if "parameterize" in dict(*caseinfo).keys():
                new_data = ddt(*caseinfo)
                return new_data

            else:
                return caseinfo

    # Logger().logger.info("读到数据===>>{}".format(data))


# @pytest.mark.parametrize("caseinfo", read_yaml("test.yaml"))
# def test_demo(caseinfo):
#     print(caseinfo)

def ddt(caseinfo):
    if "parameterize" in caseinfo.keys():
        caseiofo_str = json.dumps(caseinfo)
        print("=========")
        print(caseiofo_str)
        for param_key,param_value in caseinfo["parameterize"].items():
            key_list =param_key.split("-")
            print(key_list,param_value)
            length_flag = True
            data_list =read_yaml(param_value)
            for data in data_list:
                print(data)
                if len(data) != len(key_list):
                    length_flag = False
                    break
            new_caseinfo = []
            if length_flag:
                for x in range(1,len(data_list)):
                    temp_caseinfo =caseiofo_str

# ReadFileData().read_config_yaml(base_test_url)
ddt(read_yaml("./test.yaml"))







# def replace_value(data, *args, **kwargs):
#     # 判断data是否存在
#     print(f"参数data为：{data}")
#     if data is not None:
#         # 判断data类型是列表及字典类型则用json方法转为字符串类型
#         # print("进入到判断中")
#         if isinstance(data, list) or isinstance(data, dict):
#             # print("进入到字典或列表")
#             str_data = json.dumps(data)
#         # 判断data非字典及列表则强转为字符串即可
#         else:
#             # print("进入到其它类型")
#             str_data = str(data)
#         # print(f"当前参数：{str_data}")
#         # 对字符串str_data进行循环,判断是否存在${},存在则替换所有参数
#         for rv in range(1, str_data.count("$") + 1):  # 这里判断替换次数
#             length = len(str_data)
#             print(f"当前长度为：{length}")
#             print(f"{str_data.count('$')}")
#             start_index = str_data.index('${')
#             print(f"当前起始值为：{start_index}")
#             end_index = str_data.index('}', start_index, length + 1)
#             print(start_index, end_index)
#             print(f"当前需要替换值：{str_data[start_index:end_index + 1:]}")
#             replace_data = read_environment(f'{str_data[start_index + 2:end_index:]}')
#             if replace_data is not None:
#                 str_data = str_data.replace(str_data[start_index:end_index + 1:], str(replace_data))
#             else:
#                 print(
#                     f"您要读取替换的key值：{str_data[start_index + 2:end_index:]}，不存在请前往/test_datas/data_type/yaml/environment.yaml文件中确认")
#         return eval(str_data)
#
#     else:
#         print(f"您输入参数有误要替换的参数项为：{data}")


# if __name__ == '__main__':
#     pytest.main(["-vs","demo.py"])

# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/30 22:40
@Auth ： ZhaoQiang
@File ：pandas_merge_excel.py
@IDE ：PyCharm
"""

import pandas as pd
import os, time


def merge_excel(file_path):
    merge_data = pd.DataFrame()
    for file_name in os.listdir(file_path):
        if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
            excel_data = pd.read_excel(file_path + "\\" + file_name)
            merge_data = pd.concat([merge_data, excel_data])
    merge_data.to_excel(result_path, index=False)


'''
pandas如何实现把一个excel中的多个sheet合并为一个sheet呢，具体思路如下：
 
　　1、读取excel获取每个的sheet的DataFrame对象，通过把read_excel的sheet_name参数设为None来实现。
 
　　2、设定一个空DataFrame对象用来拼接每个sheet。
 
　　3、循环每个sheet，然后通过concat函数把空DataFrame对象依次拼接每个sheet。
'''


def merge_excel_sheets(path):
    excel_data = pd.read_excel(path, sheet_name=None)
    # 获取所有sheet名字
    # 如果read_excel参数不是None,则excel_data.keys()为表名
    sheet_names = list(excel_data.keys())
    # print(sheet_names)   ['表格1', '表格2', '表格3']
    # 创建空DataFrame用来连接
    merger_data = pd.DataFrame()
    # 遍历excel表格中的sheet表格
    for sheet_name in sheet_names:
        df_sheet = excel_data[sheet_name]
        merger_data = pd.concat([merger_data, df_sheet])
    merger_data.to_excel("result111.xlsx", index=False)


if __name__ == '__main__':
    time = time.strftime("%Y%m%d%H%M", time.localtime())
    file_path = "./data"
    result_path = "./result/" + time + ".xlsx"
    merge_excel(file_path)

    # path = "./SZ.xlsx"
    # merge_excel_sheets(path)

# -*- coding: utf-8 -*-
"""
@author:赵公子
@date:2022/7/23 22:57
@filename:demo.py
"""
import difflib
import re
from thefuzz import fuzz,process

# import sqlite3
#
#
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
#
# with open("./StockID.txt", encoding="utf-8", mode="w") as f:
#     con = sqlite3.connect("mitake.sse.sqlite.db")
#     con.row_factory = dict_factory
#     c = con.cursor()
#     c.execute("select StockID from Stock")
#     output = c.fetchall()
#     for StockID in output:
#         for key,values in StockID.items():
#             f.write(values)
#
#
# with open("./AllStock_szbh.txt",encoding="utf-8") as file,open("./AllStock_deal.txt",encoding="utf-8",mode="w") as f:
#     for str in file:
#         Str1 = str.replace("[","").replace("]","")
#         dict1 = eval(Str1)
#         for concent in tuple(dict1):
#             for key,values in concent.items():
#                 if key == "s":
#                     f.write(values)


# with open("./Stocks/stock_ine.txt",encoding="utf-8") as file,\
#         open("./AllStock_deal1.txt",encoding="utf-8",mode="a") as file1:
#     for stock in file:
#         数字+.两位小写字母形式  sh\shbh\sz\szbh\hh\hz\bj\bz\
#         stock1 = re.findall("[0-9]*.[a-z][a-z]",stock)
#         gb文件
#         stock1 = re.findall("[0-9]{6}.[a-z][a-z]|[A-Z]{6}.[a-z][a-z]|[A-Z0-9]{6}.[a-z][a-z]",stock)
#         bk文件
#         stock1 = re.findall("[A-Z0-9]{6}.[a-z][a-z]",stock)
#         hk文件
#         stock1 = re.findall("[0-9]*.[a-z][a-z]|[A-Z]*.[a-z][a-z]",stock)
#         shfe文件
#         stock1 = re.findall("[A-Z].shfe|[a-z0-9]{6}.shfe|[a-z0-9A-Z]{12}.shfe|[a-z0-9A-Z]{10}.shfe",stock)
#         cff文件
#         stock1 = re.findall("[A-Z0-9]{6}.cff|[A-Z0-9-]{13}.cff|[a-z0-9]{6}|[A-Z0-9]{5}.cff",stock)
#         czce文件
#         stock1 = re.findall("[A-Z0-9]{6}.czce|[A-Z0-9]{11}.czcef|[A-Z0-9]{5}.czce",stock)
#         dce文件
#         stock1 = re.findall("[a-z0-9]{5}.dce|[a-z0-9-A-Z]{12}.dce|"
#                             "[a-z0-9]{6}.dce|[a-z0-9-A-Z]{13}.dce|"
#                             "[a-z0-9-A-Z]{14}.dce|[a-z0-9-A-Z]{11}.dce",stock)
#         ine文件
#         stock1 = re.findall("[a-z0-9]{6}.ine|[a-z0-9A-Z]{10}.ine",stock)
#
#         for result in stock1:
#             file1.write(result)


# print("\033[1;31;43m打印设置颜色! \033[0m")
# print("\033[31m输入有误，请重新输入！\033[0m")
# print("\033[31;43m输入有误，请重新输入！\033[0m")


with open("./StockID.txt",encoding="utf-8") as file1:
    stock1 = file1.readlines()
with open("./AllStock_deal.txt",encoding="utf-8") as file2:
    stock2 = file2.readlines()
res = fuzz.token_sort_ratio(stock1,stock2)
print(res)


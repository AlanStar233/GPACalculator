# -*- coding: utf-8 -*-
"""
@File    : xlsResolver.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import pandas as pd

from xlsConfig import xlsConfig
from StatusCode import StatusCode

# 全局变量
xlsPath = "./data/" + xlsConfig.getDefaultXlsName()
if xlsConfig.getIsHaveTopBar():
    header = 0
else:
    header = None
useColumns = ["课程代码", "课程名称", "课程性质", "学分", "成绩", "绩点", "成绩性质", "成绩备注", "是否成绩作废", "课程类别", "考核方式"]

class xlsResolver:
    """
        私有方法, get 表格数据
    """
    @staticmethod
    def __getXlsArrays():
        data = pd.read_excel(xlsPath, sheet_name="sheet1", header=header, usecols=useColumns, keep_default_na=False)
        arrays = data.to_numpy()
        return arrays

    """
        get line 数
    """
    @staticmethod
    def getLine():
        return xlsResolver.__getXlsArrays().shape[0]

    """
        get columns 数
    """
    @staticmethod
    def getColumns():
        return xlsResolver.__getXlsArrays().shape[1]

    """
        通过 useColumns 中存在的对象名找到对应的下标, 返回对应的数组对象
    """
    @staticmethod
    def getColumnData(columnsName):
        columnData = []
        try:
            columnIndex = useColumns.index(columnsName)
        except ValueError:
            print(StatusCode.error() + f"{columnsName} 不存在索引!")

        for i in range(xlsResolver.getLine()):
            # 判断输入是否为 绩点 或 学分, 如果是, 就转换为 float 类型
            if columnsName == "绩点" or columnsName == "学分":
                columnData.append(float(xlsResolver.__getXlsArrays()[i][columnIndex]))
            # 否则就按正常处理
            else:
                columnData.append(xlsResolver.__getXlsArrays()[i][columnIndex])
        return columnData

if __name__ == '__main__':
    # print(xlsResolver.getColumnData("课程代码"))
    # print(xlsResolver.getColumnData("学分"))
    print(xlsResolver.getColumnData("绩点"))

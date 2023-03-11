# -*- coding: utf-8 -*-
"""
@File    : xlsConfig.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import json

"""
    对 ./config/xlsResolverConfig.json 解析
"""
class xlsConfig:
    """
        提取出 JSON Object
    """
    @staticmethod
    def configResolver():
        with open("./config/xlsResolverConfig.json", "r", encoding="utf-8") as config:
            config = json.loads(config.read())
            return config

    """
        get 欲解析的 Excel 文档的默认 sheet (一般只为1, 但也提供一个方法)
    """
    @staticmethod
    def getDefaultSheet():
        config = xlsConfig.configResolver()
        sheet = config["sheet"]
        return sheet

    """
        文档是否有 TopBar (默认有, 一般不用修改配置文件)
    """
    @staticmethod
    def getIsHaveTopBar():
        config = xlsConfig.configResolver()
        isHaveTopBar = bool(config["isHaveTopBar"])
        return isHaveTopBar

    """
        系统类型
    """
    @staticmethod
    def getOS():
        config = xlsConfig.configResolver()
        osName = config["OS"]
        return osName

    """
        get 默认文件名
    """
    @staticmethod
    def getDefaultXlsName():
        config = xlsConfig.configResolver()
        defaultXlsName = config["defaultXlsName"]
        return defaultXlsName


if __name__ == '__main__':
    print(xlsConfig.getDefaultSheet())
    print(xlsConfig.getIsHaveTopBar())
    print(xlsConfig.getOS())

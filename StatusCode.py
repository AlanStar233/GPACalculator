# -*- coding: utf-8 -*-
"""
@File    : StatusCode.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""

class StatusCode:
    @staticmethod
    def message():
        msg = "\033[92m[message]\033[0m "
        return msg

    @staticmethod
    def warning():
        msg = "\033[93m[warning]\033[0m "
        return msg

    @staticmethod
    def error():
        msg = "\033[31m[error]\033[0m "
        return msg

if __name__ == "__main__":
    print(StatusCode.message() + "这是一条普通消息")
    print(StatusCode.warning() + "这是一条警告消息")
    print(StatusCode.error() + "这是一条错误消息")

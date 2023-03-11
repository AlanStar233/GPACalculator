# -*- coding: utf-8 -*-
"""
@File    : main.py
@Author  : AlanStar
@Contact : alan233@vip.qq.com
@License : MIT
Copyright (c) 2022-2023 AlanStar
"""
import os

import keyboard
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.style import Style
from rich.table import Table

from xlsConfig import xlsConfig
from xlsResolver import xlsResolver

# 全局变量
headerTableStyle = Style(bold=True, color="#66CCFF")
defaultRowStyle = Style(color="white", bgcolor=None)
highLightRowStyle = Style(color="#66CCFF", bgcolor="white")
selectedRow = 0     # 默认选中行数初始化
markedRow = []      # 已选中的行
sigmaGP_And_Score = float(0.0)
sigmaScore = float(0.0)

# TODO: 请按照运行终端的环境来确定用 cls 或 clear 清屏, pycharm 终端已知不会对两个命令做出响应
def clearByOS(termOS):
    if termOS == "Windows":
        clearByWindows = os.system("cls")
    elif termOS == "Linux":
        clearByLinux = os.system("clear")

# 输入式表格样式更新器
def tableStyleUpdaterWithValue(lineNum):
    # 如果这行已经被选中了，就取消选中
    if lineNum in markedRow:
        markedRow.remove(lineNum)
        table.rows[lineNum].style = defaultRowStyle
    # 如果这行没有被选中，就选中它
    else:
        markedRow.append(lineNum)
        table.rows[lineNum].style = highLightRowStyle
    # 刷新表格状态
    console.clear()
    console.print(table, crop=False, overflow="ignore", soft_wrap=True)


# 键盘处理事件, 检测到 ↑ 或 ↓ 按键后光标变化, 并通过 space 和 enter 锚定和提交表格行
def keyInputHandler():
    global selectedRow, markedRow
    # 若 ↑, 且索引 > 0, 则当前选中的行是...?
    if keyboard.is_pressed("up"):
        # 如果当前选中的行是第一行，就跳到最后一行
        if selectedRow == 0:
            selectedRow = len(table.rows) - 1
        # 否则就往上移动一行
        else:
            selectedRow -= 1
        tableStyleUpdater()
        console.clear()
        console.print(table, crop=False, overflow="ignore", soft_wrap=True)
    # 若 ↓, 且索引 < 表格总长度 - 1，则当前选中的行是...?
    elif keyboard.is_pressed("down"):
        # 如果当前选中的行是最后一行，就跳到第一行
        if selectedRow == len(table.rows) - 1:
            selectedRow = 0
        # 否则就往下移动一行
        else:
            selectedRow += 1
        tableStyleUpdater()
        console.clear()
        console.print(table, crop=False, overflow="ignore", soft_wrap=True)
    # 空格控制部分
    elif keyboard.is_pressed("space") and selectedRow not in markedRow:
        markedRow.append(selectedRow)
        tableStyleUpdater()
        console.clear()
        console.print(table, crop=False, overflow="ignore", soft_wrap=True)
    elif keyboard.is_pressed("space") and selectedRow in markedRow:
        markedRow.remove(selectedRow)
        console.clear()
        console.print(table, crop=False, overflow="ignore", soft_wrap=True)


# TODO: 核心功能
clearByOS(xlsConfig.getOS())   # 先清屏一次
# __builtins__.print(StatusCode.message() + "导入数据并渲染中...")

# 创建一个 Console 对象
console = Console()

# 创建一个表格对象
table = Table(show_header=True, header_style=headerTableStyle, expand=True)
table.add_column("序号")
# table.add_column("课程代码")
table.add_column("课程名称")
# table.add_column("课程性质")
table.add_column("学分")
table.add_column("成绩")
table.add_column("绩点")
table.add_column("成绩性质")
table.add_column("成绩备注")
table.add_column("是否作废")

# 创建一个 Progress 对象, 并新增任务
progressBar = Progress(console=console)
addDataTask = progressBar.add_task("正在读取数据并渲染中...", total=xlsResolver.getLine())

# print(xlsResolver.getLine())

# 写入数据
with progressBar:
    # for i in range(xlsResolver.getLine()):
    for i in range(6):
        table.add_row(
                      str(i),
                      str(xlsResolver.getColumnData("课程名称")[i]),
                      str(xlsResolver.getColumnData("学分")[i]),
                      str(xlsResolver.getColumnData("成绩")[i]),
                      str(xlsResolver.getColumnData("绩点")[i]),
                      str(xlsResolver.getColumnData("成绩性质")[i]),
                      str(xlsResolver.getColumnData("成绩备注")[i]),
                      str(xlsResolver.getColumnData("是否成绩作废")[i]),
                      )
        progressBar.update(addDataTask, advance=1)


# 渲染完毕, 将提示消息干掉
clearByOS(xlsConfig.getOS())

# 打印表格
console.print(table, crop=False, overflow="ignore")

# 用户选中行逻辑
while True:
    lineNum = console.input("请输入选中/反选的行号, 按 Enter 结束, 输入 Q 停止选中并退出:")
    # 如果用户输入了 q 或 Q ，就退出循环
    if lineNum == "q" or lineNum == "Q":
        break
    # 如果用户输入了空字符串，就停止选中
    elif lineNum == "":
        continue
    # 如果用户输入了数字字符串，就尝试转换为整数并更新表格样式
    else:
        try:
            num = int(lineNum)
            tableStyleUpdaterWithValue(num)
        # 如果转换失败，就提示用户输入无效，并继续循环
        except ValueError:
            console.print("请输入有效的行号！")

print("--------------------")
print(f"你选中了以下行:{markedRow}")
print("--------------------")

# 计算绩点
# print(f"绩点: {xlsResolver.getColumnData('绩点')[markedRow[0]]}" + f"学分: {xlsResolver.getColumnData('学分')[markedRow[0]]}")
for rowNum in range(len(markedRow)):
    print(f"{xlsResolver.getColumnData('课程名称')[markedRow[rowNum]]} 的绩点为: {xlsResolver.getColumnData('绩点')[markedRow[rowNum]]}, 学分为: {xlsResolver.getColumnData('学分')[markedRow[rowNum]]}")
    sigmaGP_And_Score += xlsResolver.getColumnData("绩点")[markedRow[rowNum]] * xlsResolver.getColumnData("学分")[markedRow[rowNum]]
    sigmaScore += xlsResolver.getColumnData("学分")[markedRow[rowNum]]
print("--------------------")

# 输出 sigmaGP_And_Score 和 sigmaScore
print("Σ (课程绩点 x 课程学分): {:.2f}".format(sigmaGP_And_Score))
print(f"Σ 课程学分: {sigmaScore}")
print("--------------------")

# 计算 GPA 并输出
GPA = sigmaGP_And_Score / sigmaScore
print("你的 GPA 为: {:.2f}".format(GPA))
print("注: 除法运算时可能会出现精度丢失问题, 此处已保留两位小数, 你可以根据上方提供的求和结果手动运算")


# GPACalculator

> 一个<s>应该不是很好用的</s>GPA计算器

## :pill:一、适用人群	

​	使用 **正方教务系统** 的同学，且教务系统没有提供自动计算 GPA 等界面的。

​	需要可视化自己的绩点、学分和GPA的。

## :hamburger:二、食用方法

### 2.1 安装依赖库

​	以 Windows 系统为例, 你可以在工程目录下打开**终端 (Windows Terminal)**，并输入以下命令：

```shell
pip install -r ./requirements.txt
```

​	等待依赖库安装完成即可。

​	注：rich 库建议使用 10.12.0 版本，最新版本可能存在兼容性问题。

### 2.2 修改配置文件

​	你可以在 <kbd>./config</kbd>目录下找到 **xlsResolverConfig.json** 这个配置文件。

​	我在这里给出配置项和对应解释, 如有需要可自行修改。

```json
{
    "sheet": "sheet1",	// 读取的 sheet 编号, 默认为 sheet1
    "isHaveTopBar": "True",	// 导出的表格是否有表头
    "OS": "Windows",	// 操作系统, Windows/Linux
    "defaultXlsName": "data.xls"    // 导出表格名, 程序会自动在工程目录下的 data 中寻找对应文件名的文件
}
```

### 2.3 开始运行

​	在工程目录下的终端里输入:

```shell
python3 ./main.py
```

​	即可运行程序，之后按照程序引导即可。

## :wrench:三、一点问题

* 在未知情况下, 读取绩点数据时会出现返回列表为空，目前仍未找到原因。

---

<p align=center>日常摸鱼, 如果好心大佬发现了解决方案，可以发PR，不胜感激</p>
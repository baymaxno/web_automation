# -*- coding: utf-8 -*-
'''
@Time    : 2021/5/24 0024 上午 10:28
@Author  : dabai
@File    : open_app.py
'''


# 文件打包  加载第三方库 pyinstaller   去doc界面输入 pyinstaller -F xx.py

import win32api

# 打开对应文件里的exe文件
win32api.ShellExecute(0, "open", "D:\\Program Files\\DALITools\\DALIMonitor25.exe", "", "", 1)



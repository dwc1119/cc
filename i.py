import sys
import requests

import os
import shutil
import filecmp
import datetime

# 打印当前时间的函数
def print_current_time(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{message} {current_time}")

# 目标页面 URL
url = 'http://tonkiang.us/hoteliptv.php'

# 从命令行参数中获取搜索关键字

keyword == 天元围棋

# 构造 POST 请求参数
payload = {'search': keyword}

# 发送 POST 请求
response = requests.post(url, data=payload)

# 打印响应内容
print(response.text)

# 在程序结束时打印当前时间
print_current_time("程序执行完成时间：")

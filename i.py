import time
import os
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import threading
from queue import Queue
import eventlet
eventlet.monkey_patch()

###urls城市根据自己所处的地理位置修改
#urls = [
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9cWluaHVhbmdkYW8%3D",#秦皇岛
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9InRhbmdzaGFuIg%3D%3D",#唐山
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIHJlZ2lvbj0iaGViZWki",#河北
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9ImxhbmdmYW5nIg%3D%3D",#廊坊
    "https://site.ip138.com/mail.petzhu.top/"#河北
]

url = 'https://example.com'
try:
    response = requests.get(url, timeout=5)  # 设置超时时间为5秒
    response.raise_for_status()  # 检查是否请求成功
    print(response.text)
except requests.exceptions.Timeout:
    print("请求超时，请检查网络或尝试增加超时时间。")
except requests.exceptions.RequestException as e:
    print(f"请求发生异常：{e}")
    

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
urls = [
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9cWluaHVhbmdkYW8%3D",#秦皇岛
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9InRhbmdzaGFuIg%3D%3D",#唐山
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIHJlZ2lvbj0iaGViZWki",#河北
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9ImxhbmdmYW5nIg%3D%3D",#廊坊
    "https://site.ip138.com/mail.petzhu.top/"#河北
]

for url in urls:
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            print(url)
        else
        continue
    except requests.exceptions.RequestException:
        pass
    print(error)

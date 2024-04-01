import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import os
import threading
from queue import Queue
import eventlet
eventlet.monkey_patch()

url ="https://fofa.info/result?qbase64=572R57ucVFbnrqHnkIbns7vnu58%3D"

response = requests.get(url) 
#content = response.text
print （response.text）


from bs4 import BeautifulSoup 
soup = BeautifulSoup(content, "html.parser")


url = [] 
# 通过查找标签提取1直播源信息 
pattern = r'("^113.9")'
live_source = re.match(pattern,soup)  


with open("itvlist.txt", "w") as file: 
    for live_source in live_sources: 
        file.write(live_source + "\n")




import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import re
import os
import threading
from queue import Queue
import eventlet
eventlet.monkey_patch()

urls ="https://fofa.info/result?qbase64=SVBUVue7vOWQiOeuoeeQhuezu%2Be7nw%3D%3D"

response = requests.get(urls) 
content = response.text


from bs4 import BeautifulSoup 
soup = BeautifulSoup(content, "html.parser")


live_sources = [] 
# 通过查找标签提取1直播源信息 
for tag in soup.find_all("a"): 
    if tag.get("href") and "live_source" in tag.get("href"): 
        live_sources.append(tag.get("href")) 
    # 通过查找属性提取直播源信息 
for tag in soup.find_all(attrs={"class": "live-source"}): 
    live_sources.append(tag.get("src"))


with open("itvlist.txt", "w") as file: 
    for live_source in live_sources: 
        file.write(live_source + "\n")




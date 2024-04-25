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
    #"https://fofa.info/result?qbase64=572R57ucVFbnrqHnkIbns7vnu58%3D",
    #"http://tonkiang.us/",
    #"https://fofa.info/result?qbase64=IuS6v%2BmUi%2BeOi%2BWdpCI%3D",
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIGNpdHk9cWluaHVhbmdkYW8%3D",#秦皇岛
    #"https://fofa.info/result?qbase64=Iue9kee7nFRW566h55CG57O757ufIg%3D%3D"
]

def modify_urls(url):
    modified_urls = []
    ip_start_index = url.find("//") + 2
    ip_end_index = url.find(":", ip_start_index)
    base_url = url[:ip_start_index]  # http:// or https://
    ip_address = url[ip_start_index:ip_end_index]
    port = url[ip_end_index:]
    ip_end = "/rtp/239.254.201.152:7205"
    for i in range(1, 256):
        modified_ip = f"{ip_address[:-1]}{i}"
        modified_url = f"{base_url}{modified_ip}{port}{ip_end}"
        modified_urls.append(modified_url)

    return modified_urls
    


def is_url_accessible(url):
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass
    return None


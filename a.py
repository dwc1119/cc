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
    "https://fofa.info/result?qbase64=InVkcHh5IiAmJiBhc249IjQxMzQiICYmIHJlZ2lvbj0iaGViZWki",
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
    ip_end = "/status"

    modified_ip = f"{ip_address}"
    modified_url = f"{base_url}{modified_ip}{port}{ip_end}"
    modified_urls.append(modified_url)
    #print(modified_url)

    return modified_urls


def is_url_accessible(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass
    return None


results = []
if urls:
    for url in urls:
    
        # 创建一个Chrome WebDriver实例
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    
        driver = webdriver.Chrome(options=chrome_options)
        # 使用WebDriver访问网页
        driver.get(url)  # 将网址替换为你要访问的网页地址
        time.sleep(10)
        # 获取网页内容
        page_content = driver.page_source
    
        # 关闭WebDriver
        driver.quit()
    
        # 查找所有符合指定格式的网址
        pattern = r"http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"  # 设置匹配的格式，如http://8.8.8.8:8888
        urls_all = re.findall(pattern, page_content)
        # urls = list(set(urls_all))  # 去重得到唯一的URL列表
        urls = set(urls_all)  # 去重得到唯一的URL列表
        x_urls = []
        for url in urls:  # 对urls进行处理，ip第四位修改为1，并去重
            url = url.strip()
            ip_start_index = url.find("//") + 2
            ip_end_index = url.find(":", ip_start_index)
            ip_dot_start = url.find(".") + 1
            ip_dot_second = url.find(".", ip_dot_start) + 1
            ip_dot_three = url.find(".", ip_dot_second) + 1
            base_url = url[:ip_start_index]  # http:// or https://
            ip_address = url[ip_start_index:ip_dot_three]
            port = url[ip_end_index:]
            ip_end = url[ip_dot_three:ip_end_index]
            modified_ip = f"{ip_address}{ip_end}"
            x_url = f"{base_url}{modified_ip}{port}"
            x_urls.append(x_url)
            #print(x_url)
        urls = set(x_urls)  # 去重得到唯一的URL列表
    
        valid_urls = []
        #   多线程获取可用url
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            for url in urls:
                url = url.strip()
                modified_urls = modify_urls(url)
                for modified_url in modified_urls:
                    futures.append(executor.submit(is_url_accessible, modified_url))
    
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    valid_urls.append(result)

        for result in valid_urls:
            with open("ip.txt", 'w', encoding='utf-8') as file:
                file.write(result + "\n")
            with open("itvlist.m3u", 'w', encoding='utf-8') as file:
                file.write(result + "\n")
            print(result)
            udpxy_urls = []
            # 修改文件转发地址
            ip_start_index = result.find("//") + 2
            ip_dot_start = result.find(".") + 1
            ip_index_second = result.find("/", ip_dot_start)
            base_url = result[:ip_start_index]  # http:// or https://
            ip_address = result[ip_start_index:ip_index_second]
            url_x = f"{base_url}{ip_address}"
            udpxy_url = f"{url_x}"
            udpxy_urls.append(udpxy_url)
            with open("ip.txt", 'w', encoding='utf-8') as file:
                for udpxy_url in udpxy_urls:
                    file.write(udpxy_url + "\n")
            with open("itvlist.m3u", 'w', encoding='utf-8') as file:
                for udpxy_url in udpxy_urls:
                    file.write(udpxy_url + "\n")
                     
    
for udpxy_url in udpxy_urls:
    print(udpxy_url)
results = []
channel_udpxy_urls = []
with open("iptv.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        #print(line)
        result = line.strip()
        if line:
            channel_name,channel_url = result.split(",")
            for udpxy_url in udpxy_urls:
                #print(udpxy_url)
                channel_udpxy_url = f"{udpxy_url}{channel_url}"
                result=f"{channel_name},{channel_udpxy_url}"
                results.append(result)
        
                    
with open("itvlist.txt", 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result + "\n")
with open("itvlist.m3u", 'w', encoding='utf-8') as file:
    for channel in results:
        file.write(result + "\n")
    

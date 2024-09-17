import sys
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import shutil
import filecmp
import datetime
import cv2

# 打印当前时间的函数
def print_current_time(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{message} {current_time}")

# 目标页面 URL
url = 'http://tonkiang.us/hoteliptv.php'

# 搜索关键字

keyword = '河北电信'

# 构造 POST 请求参数
payload = {'search': keyword}

# 发送 POST 请求
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
    
driver = webdriver.Chrome(options=chrome_options)
        # 使用WebDriver访问网页
driver.POST(url, data=payload)  # 将网址替换为你要访问的网页地址
   # time.sleep(10)
        # 获取网页内容
response = driver.page_source
    
        # 关闭WebDriver
driver.quit()
#response = requests.post(url, data=payload)

# 打印响应内容
print(response)
html_content = response
        # 使用正则表达式匹配IP地址和端口号
ips_ports = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', html_content)
unique_ips_ports = list(set(ips_ports))  # 去除重复的IP地址和端口号
         


# 检查视频流的可达性
def check_video_stream_connectivity(ip_port, urls_udp):
    try:
        # 构造完整的视频URL
        video_url = f"http://{ip_port}{urls_udp}"
        # 用OpenCV读取视频
        cap = cv2.VideoCapture(video_url)
        
        # 检查视频是否成功打开
        if not cap.isOpened():
            print(f"视频URL {video_url} 无效")
            return None
        else:
            # 读取视频的宽度和高度
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(f"视频URL {video_url} 的分辨率为 {width}x{height}")
            # 检查分辨率是否大于0
            if width > 0 and height > 0:
                return ip_port  # 返回有效的IP和端口
            # 关闭视频流
            cap.release()
    except Exception as e:
        print(f"访问 {ip_port} 失败: {e}")
    return None           

# 定义组播地址和端口
urls_udp = "/rtp/239.254.200.45:8008"

# 提取唯一的IP地址和端口号

    #测试每个IP地址和端口号，直到找到一个可访问的视频流
for unique_ips_port in unique_ips_ports:
    valid_ip = check_video_stream_connectivity(unique_ips_port, urls_udp)
    if valid_ip:
        print(f"找到可访问的视频流服务: {valid_ip}")
        valid_ips.append(valid_ip)

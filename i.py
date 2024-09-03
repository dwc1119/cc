import requests
import re
import cv2  # 导入OpenCV库

# 定义fofa链接
fofa_url = 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJDaG9uZ3Fpbmci'
# fofa_url = 'http://tonkiang.us/hoteliptv.php?page=1&pv=%E9%87%8D%E5%BA%86%E8%81%94%E9%80%9A'

# 尝试从fofa链接提取IP地址和端口号，并去除重复项
def extract_unique_ip_ports(fofa_url):
    try:
        response = requests.get(fofa_url)
        html_content = response.text
        # 使用正则表达式匹配IP地址和端口号
        ips_ports = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', html_content)
        unique_ips_ports = list(set(ips_ports))  # 去除重复的IP地址和端口号
        return unique_ips_ports if unique_ips_ports else None
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

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

# 更新文件中的IP地址和端口号
def update_files(accessible_ip_port, files_to_update):
    for file_info in files_to_update:
        try:
            # 读取原始文件内容
            response = requests.get(file_info['url'])
            file_content = response.text

            # 替换文件中的IP地址和端口号
            # 假设文件中的IP地址和端口号格式为 http://IP:PORT
            ip_port_pattern = r'(http://\d+\.\d+\.\d+\.\d+:\d+)'
            updated_content = re.sub(ip_port_pattern, f'http://{accessible_ip_port}', file_content)

            # 保存更新后的内容到新文件
            with open(file_info['filename'], 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"文件 {file_info['filename']} 已更新并保存。")
        except requests.RequestException as e:
            print(f"无法更新文件 {file_info['filename']}，错误: {e}")

# 定义组播地址和端口
urls_udp = "/udp/225.0.4.75:7980"

# 提取唯一的IP地址和端口号
unique_ips_ports = extract_unique_ip_ports(fofa_url)

if unique_ips_ports:
    print("提取到的唯一IP地址和端口号：")
    for ip_port in unique_ips_ports:
        print(ip_port)
    
    # 测试每个IP地址和端口号，直到找到一个可访问的视频流
    valid_ip = None
    for ip_port in unique_ips_ports:
        valid_ip = check_video_stream_connectivity(ip_port, urls_udp)
        if valid_ip:
            print(f"找到可访问的视频流服务: {valid_ip}")

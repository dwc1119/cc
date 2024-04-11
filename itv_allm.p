import time
import requests
 
# ll是电视直播源的链接列表
ll=['http://110.52.99.109:85/tsfile/live/1000_1.m3u8?key=txiptv&playlive=1&authid=0','http://110.52.99.109:85/tsfile/live/1000_1.m3u8?key=txiptv&playlive=1&authid=0']
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
se=requests.Session()
 
for i in ll:
    now=time.time()
    try:
        res=se.get(i,headers=headers,timeout=5,stream=True)
        if res.status_code==200:
            for k in res.iter_content(chunk_size=1048576):
                # 这里的chunk_size是1MB，每次读取1MB测试视频流
                # 如果能获取视频流，则输出读取的时间以及链接
                if k:
                    print(f'{time.time()-now:.2f}\t{i}')
                    break
    except Exception:
        # 无法连接并超时的情况下输出“X”
        print(f'X\t{i}')

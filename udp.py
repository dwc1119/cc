import re 
url = 'https://113.215.20.136:9011/113.215.6.77/c3pr90ntcya0/youku/6981496DC9913B8321BFE4A4E73/0300010E0C51F10D86F80703BAF2B1ADC67C80-E0F6-4FF8-B570-7DC5603F9F40.flv'
pattern = 'http://(.*?):9011/'
out = re.sub(pattern, 'http://127.0.0.1:9091/', url)
print(out)

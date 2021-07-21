# 开发者 haotian
# 开发时间: 2021/7/21 11:31
import requests
from 通用部分 import headers
#所以只要把请求头 写的好一点 百度也是能爬的
url = 'https://www.baidu.com/s?wd=python'

print(headers.getHeaders())
# r = requests.get(url,headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'})
# print(r.request.url)
# print(r.text[0:2000])
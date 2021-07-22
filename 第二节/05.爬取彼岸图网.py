# 开发者 haotian
# 开发时间: 2021/7/22 11:42
import requests
from lxml import etree

url = 'https://pic.netbian.com/4k/index_2.html'

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

r = requests.get(url,headers=headers).text

tree = etree.HTML(r)

p = []

# l = len(tree.xpath('//div[@class="slist"]/ul/li/a/img/@src'))
for i in tree.xpath('//div[@class="slist"]/ul/li/a/img/@src'):
    p.append(i)

p_url = 'https://pic.netbian.com'

n_url = p_url+p[0]

r_1 =requests.get(n_url,headers = headers)

with open('../Image/tu.jpg','wb') as fp:
    fp.write(r_1.content)



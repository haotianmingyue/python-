# 开发者 haotian
# 开发时间: 2021/7/21 16:01
import requests
from lxml import etree

url = 'https://fight.qq.com'

r = requests.get(url,headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}).text

tree = etree.HTML(r)

#更新的url后缀
u_url = tree.xpath('//div[@class="i_newslist"]/ul[1]/li[1]/a[2]/@href')[0]

#新的url,得到更新内容的完整url
n_url = url+u_url
print(n_url)
#所以爬取新的更新数据
r_n = requests.get(n_url,headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'})


#千万注意文件编码
# parser = etree.HTMLParser(encoding='gbk')

tree_n = etree.HTML(r_n.text.encode('iso-8859-1').decode('gbk'))

#更新内容

r_c = tree_n.xpath('//div[@class="Section1"]//text()')

#更新时间
time = tree_n.xpath('//div[@class="cnt"]/h3/text()')[0]

print(time)

#转成字符串
r_c = ''.join(r_c)

#具体编码问题有待解决  保存文件中有   这是空格？？？
with open(f'../Data/{time}更新','w',encoding= 'utf-8') as fp:
    fp.write(r_c)
# print(r_c)


# print(n_url)
#
# print(u_url)

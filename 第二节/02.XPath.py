# 开发者 haotian
# 开发时间: 2021/7/21 13:45
from lxml import  etree

parser = etree.HTMLParser(encoding='utf-8')

#实例化对象
tree = etree.parse('deledou.html',parser = parser)
#量太大读不出来吗。。。。不是 是文件解析有问题，有的编码解析不出来？


# r = tree.xpath('/html/body/div')
#注意 如果用''会与你自己想要的意思不一样 所以用"" 效果都一样
# r = tree.xpath('//div[@class="i_newslist"]/ul[2]/li[1]/a[2]/text()')[0]
r = tree.xpath('//div[@class="i_newslist"]/ul[2]/li[1]/a[2]/@href')[0]


print(r)
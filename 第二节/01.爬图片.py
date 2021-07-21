# 开发者 haotian
# 开发时间: 2021/7/21 11:22

import  requests

url = 'https://images.pexels.com/photos/3408744/pexels-photo-3408744.jpeg'
url1 = 'https://www.pexels.com/zh-cn/discover/nature-photography/'

#1.获取页面内容
#2.使用聚焦爬虫对图片进行解析

#其实在某个url中是专门返回 图片信息的 ，里面有图片的url 可以直接通过这个url来获取图片
# https://www.pexels.com/zh-cn/medium/above-the-fold/?id%5B%5D=572897&id%5B%5D=15286&id%5B%5D=5282269&id%5B%5D=3293148&id%5B%5D=624015&id%5B%5D=3408744&id%5B%5D=3244513&id%5B%5D=3225517

# r = requests.get(url,headers={'user-agent':'Chrome/9'}).content
# with open('../Image/p1.jpeg','wb',) as fp: #注意 打开方式 是 wb 写字节   w只能写字符串
#     fp.write(r)
#     fp.close()

r1 = requests.get(url1,headers = {'user-agent':'Chrome/9'})
print(r1.text)
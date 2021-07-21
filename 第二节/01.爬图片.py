# 开发者 haotian
# 开发时间: 2021/7/21 11:22

import  requests

url = 'https://images.pexels.com/photos/3408744/pexels-photo-3408744.jpeg'

r = requests.get(url,headers={'user-agent':'Chrome/9'}).content
with open('../Image/p1.jpeg','wb',) as fp: #注意 打开方式 是 wb 写字节   w只能写字符串
    fp.write(r)
    fp.close()
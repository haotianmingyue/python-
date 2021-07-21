# 开发者 haotian
# 开发时间: 2021/7/21 9:16
import  requests
import json
#关键是找到 返回数据的url

url = 'https://www.shanghairanking.cn/rankings/bcur/2020' #官网首页地址 并不能获取到具体数据

url1 = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2020'#这是解析出来返回json 数据的地址



# r = requests.get(url,headers = {'user-agent':'Chrome/9'})   #这里直接返回页面的框架什么东西都没有
# r.encoding = r.apparent_encoding
#
# with open('./zuihaodaxue.html','w',encoding='utf-8') as fp:
#     fp.write(r.text)

r1 = requests.get(url1,headers = {'user-agent':'Chrome/9'}).json()  #注意加了 json（）方法后获得是一个字典？？
# print(r1)

# for rank in r1['data']['rankings']:
#     print(rank['univNameCn'])     #显示大学名字


univName = ""
url2 = f'https://www.shanghairanking.cn/api/v2010/inst/{univName}' #这是返回学校详情json的地址 注意univName大学英文名字 具体可以从爬取的数据中得到

# 你可以一个 for 直接把所有大学的详情全爬下来 也没什么东西就是了

#所以我们来把它保存为json文件看看效果

with open('./daxuepaiming.json','w',encoding= 'utf-8') as fp1:
    fp1.write(json.dumps(r1,indent=1,ensure_ascii=False))  #格式化   这里会把中文还原成编码 所以 要加ensure_ascii=False


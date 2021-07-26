# 开发者 haotian
# 开发时间: 2021/7/23 16:37
#目标爬飞哥与小佛  ！！！！！

import requests
from lxml import etree

import json

from multiprocessing.dummy import Pool

#视频首页
b = '1'

#经过观察发现其url命名很有特点 ，而具体视频地址则没有继承这个优良传统，遗憾
#好把 它视频地址 好像不是从 主页直接加载出来的
#<div class="stui-player__video clearfix">
# 	<script type="text/javascript">var player_aaaa={"flag":"play","encrypt":0,"trysee":0,"points":0,"link":"\/iqiyi46006-1-1.html","link_next":"\/iqiyi46006-1-5.html","link_pre":"\/iqiyi46006-1-3.html","url":"https:\/\/video.buycar5.cn\/20201020\/wPpgUW6b\/index.m3u8","url_next":"https:\/\/video.buycar5.cn\/20201020\/p3kXvEPH\/index.m3u8","from":"dbm3u8","server":"","note":"","id":"46006","sid":1,"nid":4}</script><script type="text/javascript" src="/static/js/playerconfig.js?t=20210723 1653"></script><script type="text/javascript" src="/static/js/player.js?t=a20210723 1653"></script>
#</div>  这里面的link就是视频播放的地址 nextlink 是下一个视频播放的地址
#所以我们要把它提取出来,,,,提取出来是个 赋值语句啊  ，还要提取里面的地址 ，有什么简便方法没？？？


url = f'https://www.anyooh.com/iqiyi46006-1-{b}.html'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}
#代理 。。。。

r_1 = requests.get(url,headers = headers)

# print(r_1.request.url)
tree_1 = etree.HTML(r_1.text)

url_n = tree_1.xpath('//div[@class="stui-player__video clearfix"]/script[1]/text()')

print(url_n[0])
print(len(url_n[0]))
#真的好绕啊
uu = json.loads(url_n[0][16:])
# print(uu)
#终于的到视频的 后面的url 之后还要拼装
# print(uu['url'])

#视频地址前缀
url_p = 'https://jx.444662.cn/m3u8/?url='

#所以完整视频地址
url_t = url_p+uu['url']

print(url_t)

#所以我们得到了视频的完整源地址，怎么下载呢？？


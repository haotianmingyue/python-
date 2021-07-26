# 开发者 haotian
# 开发时间: 2021/7/23 16:37
#目标爬飞哥与小佛  ！！！！！

import requests
from lxml import etree
import json
import time

from multiprocessing.dummy import Pool
def  get_m3u8(b):
    #视频首页
    # b = '1'

    # proxies = {
    #     "http": "http://140.255.139.63:3265",
    #     "https": "http://140.255.139.63:3265",
    # }

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

    # print(url_n[0])
    # print(len(url_n[0]))
    #真的好绕啊，当然你也可以用正则表达式。。。。
    uu = json.loads(url_n[0][16:])
    # print(uu)
    #终于的到视频的 后面的url 之后还要拼装
    # print(uu['url'])
    print('爬取第',b,'个')
    return uu['url']

    # #视频播放器地址前缀
    # url_p = 'https://jx.444662.cn/m3u8/?url='
    #
    # #所以完整视频地址
    # url_t = url_p+uu['url']
    #
    # print(url_t)

    #所以我们得到了视频的完整源地址，怎么下载呢？？

    #好吧我们只得到了一个播放器的地址，具体在查
    # data = requests.get(uu['url'],headers = headers).text
    #
    # print(data)

    #https://video.buycar5.cn/20201020/3DC2dKCB/index.m3u8，这样看来我们原先的得到的 视频地址，不需要拼接，只需要后半段即可
    #即 uu['url']就是视频地址，也不是地址，只是视频目录地址
    #里面 https://video.buycar5.cn/20201020/3DC2dKCB/1000kb/hls/index.m3u8?skipl=1，是视频目录地址
    #视频文件为 m3u8 ，会有许多 文件片，，，所以要 把这些文件全下载下来 ，再拼接起来吗？？？

    # data1 = requests.get('https://video.buycar5.cn/20201020/3DC2dKCB/1000kb/hls/index.m3u8?skipl=1',headers = headers)
    #
    # print(data1.text)

    # with open('../Data/飞哥与小佛第一集.m3u8','wb') as fp:
    #     fp.write(data)
    #     print("下载成功")

    #600多个ts碎片 下载下来还要自己 合成mp4  实在不行  我们 放弃吧
    #可以用 m3u8 下载工具 直接对uu['url']这个链接下载。工具下载地址 https://xyyx.lanzoui.com/iSQf1pbqr8h

    #所以我们只要对 视频链接进行提取就可以了。。 即 把 b 加一个for循环 从 1到 64 获取 m3u8的地址
    #其实我们也可以从 m3u8文件的索引中得到 ts 文件的下载地址，完全可以自己把ts文件下载下来，难得是自己组合？？

m3 = []

if __name__ == '__main__':
    for b in range(64):
        m3.append(get_m3u8(b+1))
        print(m3[b])
        # time.sleep(30) #睡眠
    with open('../Data/飞哥与小佛m3u8文件目录列表.json','w') as fp:
        fp.write(json.dumps(m3,ensure_ascii=False))
#这样





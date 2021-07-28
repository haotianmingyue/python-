# 开发者 haotian
# 开发时间: 2021/7/26 17:37
import json

from selenium import webdriver
from time import sleep
from lxml import  etree
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#发请求
driver.get('https://ui.ptlogin2.qq.com/cgi-bin/login?appid=614038002&style=9&s_url=https%3A%2F%2Fdld.qzapp.z.qq.com%2Fqpet%2Fcgi-bin%2Fphonepk%3Fcmd%3Dindex%26channel%3D0')
#功能字典
dic = {}
def back_home():
    driver.find_element_by_link_text('返回大乐斗首页').click()

#出错界面上会有返回这个链接
def error():
    return driver.find_element_by_link_text('返回')


#分析来看 决定活动领奖的 subtype 的值 88是神魔转盘  ，124 是开心娃娃机，56是登录有礼
def shenmo_zhuanpan():
    try:
        url_sz = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=newAct&subtype=88&op=1'
        driver.get(url_sz)
        back_home()
    except:
        print('神魔转盘出错')
def cai_danshuang():
    try:
        #value 2是双数 1 是单数，这里默认全双
        url_ds = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=oddeven&value=2'
        for i in range(5):
            driver.get(url_ds)
            sleep(1)
        back_home()
    except:
        print('猜单双出错')


def wawa_ji():
    try:
        url_wj = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=newAct&subtype=124&op=1'
        driver.get(url_wj)
        back_home()
    except:
        print('开心娃娃机')

def xianwu_xiuzhen(): #具体挑战还没做
    try:
        #领取活跃度80的次数
        url_lc = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=immortals&op=getreward&taskid=1'
        driver.get(url_lc)

    except:
        print('仙武修真出错')

def wulin():
    try:
        url_wl = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=fastSignWulin&ifFirstSign=1'
        driver.get(url_wl)
        #人满了点 继续报名
        driver.find_element_by_link_text('继续报名').click()
        back_home()
    except:
        print('武林大会出错')

def lingjiang():
    try:
        # 1是小 2是中 3 是大 4是终极
        def do(i):
            url_lj = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=liveness_getgiftbag&giftbagid={i}&action=1'
            driver.get(url_lj)
        do(1)
        sleep(1)
        do(2)
        sleep(1)
        do(3)
        sleep(1)
        do(4)
        sleep(1)
        back_home()
    except:
        print('领奖出错')

def jiebai_zhengba():
    try:
        url_jz = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=2540097595&B_UID=0&sid=&channel=0&g_ut=1&cmd=brofight&subtype=0'
        driver.get(url_jz)
        # 4 是无限制
        url_bm = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=2540097595&B_UID=0&sid=&channel=0&g_ut=1&cmd=brofight&subtype=1&gidIdx=4'
        driver.get(url_bm)
        back_home()
    except:
        print("结拜报名出错")

def shangdian_huanhun():  #商店买还魂丹凑活跃度
    try:
        url_bh = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=viewgoods&id=3089&pay_type=7'
        driver.get(url_bh)
        #购买还魂丹
        driver.find_element_by_xpath('//input[@type="button" and @value="兑换"]').click()
        back_home()

    except:
        print('商店买还魂丹出错')

def fenxiang():
    try:
        #一键分享
        url_fx = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sharegame&subtype=6'
        driver.get(url_fx)
        #斗神塔的分享
        url_ds = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sharegame&subtype=2&shareinfo=4'
        back_home()
    except:
        print('分享出错')

def huiliu_zhaohui():
    try:
        #召回页面
        url_zh = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=callback&subtype=3&page=1'
        driver.get(url_zh)
        #召回三次,  后面还有个空格真的。。。。。
        for i in range(3):
            driver.find_element_by_link_text('回来玩吧！').click()
        back_home()
    except:
        print('召回出错')

def mibao():
    try:
        #高级
        url_mb1 = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=tenlottery&op=2&type=0'
        #极品
        url_mb2 = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=tenlottery&op=2&type=1'
        #就是换了个 type 的值而已

        driver.get(url_mb1)
        driver.get(url_mb2)
        back_home()

    except:
        print('邪神秘宝出错')

def bangpai_gongfeng():
    try:
        #主要是id 标识 物品 3089 是 还魂丹  page 不关键只是和显示有关
        url_gf = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=oblation&id=3089&page=3'
        driver.get(url_gf)
        back_home()
    except:
        print('供奉出错')

def kuangdong():
    try:
        #矿洞领奖
        url_kl = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=factionmine&op=reward'
        driver.get(url_kl)
        #挑战
        url_tz = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=factionmine&op=fight'
        for i in range(3):
            driver.get(url_tz)
        back_home()
    except:
        print('矿洞出错')


def lueduo():
    try:
        #1 是报名，6是领取胜负奖励
        def do(i):
            url_lm = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=forage_war&subtype={i}'
            driver.get(url_lm)
        try:
            #报名
            do(1)
            #领奖
            do(6)

        except:
            print('报名领奖')
        #最后的 id 代表掠夺的 位置   313 小粮仓   ，205 中粮仓， 102 大粮仓 的 起止数
        try:
            url_ld ='https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=forage_war&subtype=4&gra_id=313'
            for i in range(40):
                driver.get(url_ld)
                sleep(1)
                if error():
                    break
            back_home()
        except:
            print('抢夺粮仓出错')

    except:
        print('掠夺出错')
def tiguan():
    try:
        #观察发现也是subtype的值控制功能 领奖 7，试炼 2，高倍转盘 4，领取奖励 13,挑战 3
        def do(i):
            url = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=facchallenge&subtype={i}'
            driver.get(url)
        #试炼5次
        for i in range(5):
            do(2)
        #挑战前高倍
        do(4)
        # 挑站
        for i in range(20):
            do(3)
        #领奖
        do(13)
    except:
        print('踢馆出错')

def jingji_chang():
    #竞技场还没开先 略过
    pass



def shier_gong():
    try:
        #为了便捷 先只使用一键扫荡功能, 最后的scene_id决定扫荡场景 1011 是扫荡双鱼，选择猴王
        #具体可以自己写函数改
        url_sd= 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=zodiacdungeon&op=autofight&scene_id=1011&pay_recover_times=0'
        driver.get(url_sd)
        back_home()
    except:
        print('十二宫出错')

def doushen_ta():
    try:
        #结束挑战
        url_js = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=towerfight&type=7&confirm=1'
        driver.get(url_js)
        #自动挑战 type 1自动挑战 2复活
        url_zd = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=towerfight&type=1'
        driver.get(url_zd)
    except:
        print('斗神塔出错')

def biaoxing_tianxia():
    try:
        def do(i):
            url_bx = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=cargo&op={i}'
            driver.get(url_bx)
        #护送完成
        do(15)
        # url_hf = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=cargo&op=15'
        # driver.get(url_hf)
        #领奖
        # url_lj = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=cargo&op=16'
        # driver.get(url_lj)
        do(16)
        #经过观察发现 控制代码是 op=的值
        #押镖  op=7  ， 刷新 3 ， 启程 6， 刷新镖师 8
        #这里还没想好怎么判断刷新的镖师是谁
        # do(7)
        back_home()
    except:
        print('押镖出错')

def piaomiao_huanjing():
    try:
        driver.find_element_by_link_text('幻境').click()
        #先返回
        driver.find_element_by_link_text('返回飘渺幻境').click()
        #进入你最高级的副本
        driver.find_elements_by_xpath('//div/p/a')[-3].click()
        #打怪 还没写
        for i in range(5):
            driver.find_element_by_link_text('乐斗').click()
            sleep(1)

        back_home()
    except:
        print('幻境出错')

def qunxiong():
    try:
        #报名
        url_s = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=thronesbattle&op=signup'
        driver.get(url_s)
        #领奖
        url_l = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=thronesbattle&op=drawreward'
        driver.get(url_l)
        back_home()
    except:
        print('群雄出错')


def huajuan_mizong():
    try:
        #分析url，buff是选择的buff，1代表选择第一个buff ，2.。。。
        #所以我们尽量用上,当然 也可以多打几次，不过 打穿也就 这几次，注意  buff 用完之后就是0
        for i in range(6):
            url_h = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=scroll_dungeon&op=fight&buff={i+1}'
            driver.get(url_h)
    except:
        print('画卷出错')


def menpai():  #实际上有的任务 例如 修炼心法的 还没写
    try:
        #进入链接门派挑战堂主的地方
        url_d = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect&op=showcouncil'
        driver.get(url_d)
        #挑战掌门首座堂主
        for i in range(7):
            driver.find_element_by_xpath(f'//div/p/a[{i+1}]').click()
        #木桩
        url_m = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect&op=trainingwithnpc'
        driver.get(url_m)
        #同门
        for i in range(2):
            url_t = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect&op=trainingwithmember'
            driver.get(url_t)
        #上香
        url_x = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect&op=fumigatefreeincense'
        driver.get(url_x)
        #上高香
        url_g = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect&op=fumigatepaidincense'
        driver.get(url_g)
        #完成任务
        url_m = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sect_task'
        driver.get(url_m)
        m = ['1','2','3']
        #总共 有8个a标签 我们需要其中的 1 3 5标签是完成任务,然而不能这样定位，一旦点击后元素位置就发生了变化，所以是 1，2，3
        for i in m:
            driver.find_element_by_xpath(f'//div/p/a[{i}]').click()
        back_home()

    except:
        print('门派出错')



def jitan():
    try:
        #只是单纯 转动  具体功能 还要收集数据
        url_j = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=altar&op=spinwheel'
        driver.get(url_j)
        '//dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=altar&op=dosteal&id=18914'
    except:
        print('祭坛出错')

def huiwu():
    try:
        #会武攻击只有这一个url 所以 要多次点击
        url_hw = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sectmelee&op=dotraining'
        try:
            #打十五次
            for i in range(15):
                driver.get(url_hw)
        except:
            print('挑战中死亡')
        #第二次挑战
        try:
            #打十五次
            for i in range(5):
                driver.get(url_hw)
        except:
            print('第二次挑战中死亡')
        #助威丐帮
        url_gb = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=sectmelee&op=cheer&sect=1003'
        driver.get(url_gb)
        back_home()


    except:
        print('会武出错')
def mengxiang_zhilv():
    try:
        #普通旅行
        url_ml = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=dreamtrip&sub=2'
        driver.get(url_ml)
        back_home()
        #梦幻旅行 url_mh = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=dreamtrip&sub=2&smapid=1'
        #只需要改变mapid即可
        #而//dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=dreamtrip&sub=0&bmapid=1
        #这里 mapid是 决定东南西北 sub 决定 具体还是大地图
    except:
        print('梦旅出错')

def wending():
    print('weizuo')

def bangpai_shanghui():
    try:
        #这里应该是gift_id定位 奖励,具体id 还要多积累
        url_bs = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=fac_corp&op=3&gift_id=667&type=0'
        driver.get(url_bs)
    except:
        print('帮派商会出错')




#联赛参站要打人 是qq号标识的
def huangjin_liansai():
    try:
        #领取奖励
        url_lj = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=factionleague&op=5'
        driver.get(url_lj)
        # #参战 具体还有问题 后面再考虑
        # driver.find_element_by_link_text('参战').click()
        # sleep(1)
        # #所以可攻击的a标签的个数=总个数-3（规则，返回上一页，返回首页）
        # #所以我们点击 a[1]-a[len-3]
        #
        # # len = len()
        # # print(len(driver.find_elements_by_xpath('//div/p//a')))
        # l = len(driver.find_elements_by_xpath('//div/p//a'))
        # # print(l)
        # for i in range(2,l-1):
        #     #攻击
        #     driver.find_element_by_xpath(f'//div/p/a[{i}]').click()
        #     sleep(1)
        #     #先这么写把具体看情况
        #     # if driver.current_url == 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=factionleague&op=4&opp_uin=974796897'
        #     #     back_home()
        #     #     break
        #     # else:
        #     #     continue
        #     try:
        #         driver.find_element_by_link_text('返回联赛')
        #     except:
        #         print('未死亡')


        back_home()
    except:
        print('黄金联赛领取奖励失败')


def xiashi_kezhan():
    try:
        #领取二楼奖励
        n = ['1','2','3']
        for i in n:
            url_t = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=warriorinn&op=getlobbyreward&type=2&num={i}'
            driver.get(url_t)
            sleep(1)
        back_home()
        # '//dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=warriorinn&op=confirmadventure&pos=0&type=0'
        # '//dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=warriorinn&op=confirmadventure&pos=1&type=0'
        # '//dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=warriorinn&op=exceptadventure&pos=1'
    except:
        print('领取奖励出错')




def xialv_boss():
    #同帮派boss
    try:
        #和好友boss一样 关键是 B_UID的值 标识每一个boss
        #  圣 盗 贼 三 四 大

        xb = ['153','18','17','152','15','13']
        for i in xb:
            url_bb = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=fight&B_UID={i}&page=&type=10'
            driver.get(url_bb)
            sleep(1)
        back_home()
    except:
        print('乐斗侠侣boss出错')



def bangpai_boss():
    try:
        #和好友boss一样 关键是 B_UID的值 标识每一个boss
        # 羊 教 帅 姜 月 源
        bb = ['10','2','3','4','5','6']
        for i in bb:
            url_bb = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=fight&B_UID={i}&page=1&type=2'
            driver.get(url_bb)
            sleep(1)
        back_home()
    except:
        print('乐斗帮派boss出错')

def tudi_exp():
    driver.find_element_by_link_text('领取徒弟经验').click()

def meiri_jiangli():
    try:
        mj = ['login','meridian','daren','wuzitianshu']
        #同理关注key的值
        for i in mj:
            url_mj = f'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=dailygift&op=draw&key={i}'
            driver.get(url_mj)
            sleep(1)
        back_home()
    except:
        print('每日奖励出错')





def men_pai():
    try:
        #门派邀请
        url_menpai_yaoqing = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=secttournament&op=signup'
        driver.get(url_menpai_yaoqing)
        back_home()
    except:
        print('门派邀请出错')



def li_lian():
    try:
        #注意让我们来分析一下这个url，其中mapid代表地图，npcid代表boss 这里 6是代表摩云山，6114代表韦小宝
        #mapid 1-20 npid 6000-6394，注意页码
        url_song_jiang = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=mappush&subtype=3&mapid=6&npcid=6114&pageid=2'
        for i in range(3):
            #直接get这个url会直接跳到这个页面
            driver.get(url_song_jiang)
            sleep(1)
        #扫地僧
        url_sd = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=mappush&subtype=3&mapid=7&npcid=6134&pageid=2'
        for i in range(2):
            #直接get这个url会直接跳到这个页面
            driver.get(url_sd)
            sleep(1)
        driver.find_element_by_link_text('返回大乐斗首页').click()
    except:
        print('历练出错')
        driver.find_element_by_link_text('返回大乐斗首页').click()


def mission():
    try:
        driver.find_element_by_link_text('任务').click()
        sleep(1)
        driver.find_element_by_link_text('一键完成任务').click()
        sleep(1)
        driver.find_element_by_link_text('返回大乐斗首页').click()
    except:
        print('任务出错')

def friend():
    try:
        driver.find_element_by_link_text('好友').click()
        sleep(1)
        #乐斗是根据B_UID= ‘’来定位的 一般人 这里是QQ号 ，特殊boss 有自己的编码，所以我们能通过直接该这个值来达到攻击目的，注意cmd=fight是乐斗
        #打前四个  //dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=fight&B_UID=33&page=1&type=1
        uid = ['33','16','12','11']
        try:
            for i in uid:
                url_boss = f"https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=fight&B_UID={i}&page=1&type=1"
                driver.get(url_boss)
                sleep(1)
        except:
            print('挑战boss出错')
        driver.find_element_by_link_text('返回大乐斗首页').click()
    except:
        print('好友出错')


def login():
    with open('../Data/qq.json', 'r') as fp:
         a = json.load(fp)
    # print(a['qq'])
    u = driver.find_element_by_id('u')
    p = driver.find_element_by_id('p')
    u.send_keys(a['qq'])
    p.send_keys(a['pw'])
    go = driver.find_element_by_id('go')
    go.click()

    #不加sleep 会因为 iframe 没加载出来 而报错
    sleep(1)
    try:
        #登录滑块验证
        driver.switch_to.frame('tcaptcha_iframe')
        tcaptcha_drag_thumb = driver.find_element_by_id('tcaptcha_drag_thumb')
        action = ActionChains(driver)
        action.click_and_hold(tcaptcha_drag_thumb)
        for i in range(4):
            action.move_by_offset((i+1)*43, 0).perform()
        # action.key_up()
        action.release()
    except:
        print('没有滑块验证')

    sleep(2)

    #用etree得到 driver.page_source
    tree = etree.HTML(driver.page_source)
    ls = tree.xpath('//a/@href')
    la = tree.xpath('//a/text()')

    #获取列表要用 elements   ，element 只能获取第一个

    # ls = driver.find_element_by_xpath('//a/@href')
    # ls = driver.find_elements_by_tag_name('a')
    # tree = etree.HTML()
    #
    # for (s,a) in ls,la:
    #     print(a,s)
    # print(la)
    # print(ls)



    for i in range(len(la)):
        # print(la[i],ls[i])
        dic[la[i]] = ls[i]
    with open('../Data/QQFight.json','w',encoding= 'utf-8') as fp:
        json.dump(dic,fp,ensure_ascii= False)
    # print(dic)

if __name__ == '__main__':
    login()
    # friend()
    # li_lian()
    # men_pai()
    # meiri_jiangli()
    # tudi_exp()
    # bangpai_boss()
    # xialv_boss()
    # xiashi_kezhan()
    # huangjin_liansai()
    # mengxiang_zhilv()
    # huiwu()
    # menpai()
    # huajuan_mizong()
    # piaomiao_huanjing()
    # baoxing_tianxia()
    # doushen_ta()
    # shier_gong()
    # lueduo()
    # kuangdong()
    # bangpai_gongfeng()
    # mibao()
    # huiliu_zhaohui()
    # fenxiang()
    # shangdian_huanhun()
    # jiebai_zhengba()
    # mission()
    # lingjiang()
    # wulin()
    # wawa_ji()
    # shenmo_zhuanpan()
    cai_danshuang()
    # driver.get('https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=broadcast')
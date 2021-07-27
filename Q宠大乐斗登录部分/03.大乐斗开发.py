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
    friend()
    # driver.get('https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=broadcast')
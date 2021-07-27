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
        print('no ')

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
    # driver.get('https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=broadcast')
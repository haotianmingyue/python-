# 开发者 haotian
# 开发时间: 2021/7/23 16:18
import  time
#线程池
from multiprocessing.dummy import Pool
pool = Pool(8)

l=[1,2,3,4,5,6]

def addd(a):
    time.sleep(2)
    print('正在执行',a)
    time.sleep(2)
    print('执行完毕',a)

#将a列表中的每一个元素 传到 addd函数中 执行
pool.map(addd,l)
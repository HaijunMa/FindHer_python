'''
Title: Find Her
@author: Haijun Ma
Time:2018/10/12
'''

import time
def searchInBaidu():
    print('众里寻她千百度')

def returnMyHead():
    time.sleep(2)
    print('蓦然回首')
    return 1

def discoverTheLoveInDark():
    print('那人却在灯火阑珊处')

if __name__ == "__main__":
    flag = 1
    for i in range(5201314):
        searchInBaidu()   #众里寻她千百度
        time.sleep(2)
        if (flag == returnMyHead()):   #蓦然回首
            time.sleep(2)
            discoverTheLoveInDark()    #那人却在灯火阑珊处
        time.sleep(2)
            #return




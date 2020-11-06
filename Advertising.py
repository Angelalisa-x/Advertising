# coding=utf-8

import csv, requests, re
import shutil
import os

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
from GoodbyeAds import GoodbyeAds
from E7KMbb import E7KMbb
from ProAdblock import ProAdblock
from Blackmatrix7 import Blackmatrix7
from AdGuardDNS import AdGuardDNS
from FindDuplicate import FindDuplicate
from WhiteList import WhiteList



if __name__ == '__main__':
    Blackmatrix7.pull()
    GoodbyeAds.pull()
    E7KMbb.pull()
    ProAdblock.pull()
    AdGuardDNS.pull()

    strWhite = []
    strWhite = WhiteList.pull()
    #print(strWhite)

    strWhite2 = []
    strWhite2 = WhiteList.pull2()

    strWhite3 = []
    strWhite3 = WhiteList.pull3()

    #去重
    readPath='11.txt'
    writePath='cnews.test2.txt'
    lines_seen=set()
    outfiile=open(writePath,'w+')
    f=open(readPath,'r')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)

    outfiile.close()
    f.close()

    #Blackmatrix7 进行处理
    with open("Blackmatrix7.list", 'w') as f:
        for line in open("77.txt"):
            str=[]
            str = line
            str = str[0:str.find('/n')]
            str1 = str[str.find(',')+1: str.rfind(',')]
            if "#" in line:
                continue
            if line in ['\n','\r\n']:
                continue
            if line.strip() == "":
                continue
            if str1 in strWhite:
                #print(str)
                continue
            if str1 in strWhite2:
                #print(str)
                continue
            if str1 in strWhite3:
                continue
            # if "HOST,p3.pstatp.com,AdvertisingTest" in str:
            #     continue

            str = str + "\n"
            f.write(str)
    f.close()

    #文本行数
    num = 0
    with open("7.txt", 'r') as f:
        num = sum(1 for line in f)
        print('总行数为%s行。' % num)
    f.close()


    count = 0
    #格式
    with open("11.txt","w") as fin:
        #for line in open("cnews.test2.txt"):
        file = open("cnews.test2.txt","r")
        for num1,line in enumerate(file):
            str=[]
            str = line
            str = str[0:str.find('/n')]
            if num1 < num-1:
                if "meituan.net" == str:
                    #print(str)
                    count +=1
                    continue
                if "api.ksapisrv.com" == str:
                    count +=1
                    continue

                if "www.ksapisrv.com" == str:
                    count +=1
                    continue
                if "music.126.net" == str:
                    count +=1
                    continue
                if str in strWhite:
                    count +=1
                    #print(str)
                    continue
                if str in strWhite2:
                    count +=1
                    #print(str)
                    continue
                if str in strWhite3:
                    count +=1
                    continue
                else:
                    if "meituan.net" == str:
                        #print(str)
                        continue
                    if "api.ksapisrv.com" == str:
                        continue

                    if "www.ksapisrv.com" == str:
                        continue
                    if "music.126.net" == str:
                        continue
                    if str in strWhite:
                        #print(str)
                        continue
                    if str in strWhite2:
                        #print(str)
                        continue
                    if str in strWhite3:
                        continue

            str = "HOST-SUFFIX," + str
            str = str + ",REJECT" + "\n"
            fin.write(str)
        file.close()
        fin.close()


    print('count: %s' %count)
    file = open("11.txt","r")
    with open("Advertising.list","w") as fin:
        for num1,value in enumerate(file):
            if(num1 >= num-count-1):
                if ".," in value:
                    continue

                fin.write(value)
            #print("the nume:%s,the value is %s", num, value)
    file.close()
    fin.close()


    
    os.remove("1.txt")
    os.remove("11.txt")
    os.remove("7.txt")
    os.remove("77.txt")
    os.remove("cnews.test2.txt")
    shutil.rmtree("__pycache__")
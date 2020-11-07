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
from jdlingyu import jdlingyu
from kbsml import kbsml


def whiteListPro(num):
    file = open("WhiteList.txt","r")
    for num1,line in enumerate(file):
        if num1 == num:
            #print("line:",line)
            return line


if __name__ == '__main__':
    Blackmatrix7.pull()
    GoodbyeAds.pull()
    #E7KMbb.pull()
    ProAdblock.pull()
    AdGuardDNS.pull()
    jdlingyu.pull()
    #kbsml.pull()

    strWhite = []
    strWhite = WhiteList.pull()
    #print(strWhite)

    strWhite2 = []
    strWhite2 = WhiteList.pull2()

    # strWhite3 = []
    # strWhite3 = WhiteList.pull3()

    strWhite4 = []
    strWhite4 = WhiteList.pull4()

    # strWhite5 = []
    # strWhite5 = WhiteList.pull5()

    strWhite6 = []
    strWhite6 = WhiteList.pull6()

    # strWhite7 = []
    # strWhite7 = WhiteList.pull7()


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

#white 去重
    readPath='WhiteList_1.txt'
    writePath='WhiteList.txt'
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
    with open("Blackmatrix7.txt", 'w') as f:
        for line in open("77.txt"):
            str=[]
            str = line
            str = str[0:str.find('/n')]
            str1 = str[str.find(',')+1: str.rfind(',')]
            if "#" in line:
                continue
            if "*" in line:
                continue
            if line in ['\n','\r\n']:
                continue
            if line.strip() == "":
                continue
            if str1 in strWhite:
                #print(str)
                continue
            # if str1 in strWhite2:
            #     #print(str)
            #     continue
            # if str1 in strWhite3:
            #     continue
            # if str1 in strWhite4:
            #     continue
            # if str1 in strWhite5:
            #     continue
            # if str1 in strWhite6:
            #     continue
            # if str1 in strWhite7:
            #     continue
            # if "HOST,p3.pstatp.com,AdvertisingTest" in str:
            #     continue

            str = str + "\n"
            f.write(str)
    f.close()

    #文本行数
    static_num = 0
    with open("7.txt", 'r') as f:
        static_num = sum(1 for line in f)
        print('总行数为%s行。' % static_num)
    f.close()


#white hangshu 
    static_white_num =0
    with open("WhiteList.txt", 'r') as f:
        static_white_num = sum(1 for line in f)
        print('总行数为%s行。' % static_white_num)
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
            if num1 < static_num-1:
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
                # if str in strWhite2:
                #     count +=1
                #     #print(str)
                #     continue
                # if str in strWhite3:
                #     count +=1
                #     continue
                # if str in strWhite4:
                #     count +=1
                #     continue
                # if str in strWhite5:
                #     count +=1
                #     continue
                # if str in strWhite6:
                #     count +=1
                #     continue
                # if str in strWhite7:
                #     count +=1
                #     continue
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
                    # if str in strWhite2:
                    #     #print(str)
                    #     continue
                    # if str in strWhite3:
                    #     continue
                    # if str in strWhite4:
                    #     continue
                    # if str in strWhite5:
                    #     continue
                    # if str in strWhite6:
                    #     continue
                    # if str in strWhite7:
                    #     continue

            str = "HOST-SUFFIX," + str
            str = str + ",REJECT" + "\n"
            fin.write(str)
        file.close()
        fin.close()


    print('count: %s' %count)
    file = open("11.txt","r")
    with open("Advertising.txt","w") as fin:
        for num1,value in enumerate(file):
            if(num1 >= static_num-count-1):
                if ".," in value:
                    continue

                fin.write(value)
            #print("the nume:%s,the value is %s", static_num, value)
    file.close()
    fin.close()

##########################################################################
#white过滤
    ctrl = 0
    ctrl_1 = 0
    file_1 = open("Blackmatrix7_1.list","w")

    while ctrl < static_white_num:
        whiteline = []
        whiteline = whiteListPro(ctrl)
        whiteline = whiteline[0:whiteline.find("\n")]
        #print(whiteline)
        for line in open("Blackmatrix7.txt"):
            str = []
            str = line
            
            if (str.find(whiteline) >= 0):
                file_1.write(line)
                ctrl_1 +=1

        ctrl += 1
    file_1.close()

    #white hangshu 
    # static_white_num_2 =0
    # with open("Blackmatrix7_1.list", 'r') as f:
    #     static_white_num_2 = sum(1 for line in f)
    #     print('总行数为%s行。' % static_white_num_2)
    # f.close()


    with open("Blackmatrix7_1.list", 'a+') as f:
        for line in open("Blackmatrix7.txt"):
            f.write(line)
    f.close()

#white 去重
    readPath='Blackmatrix7_1.list'
    writePath='Blackmatrix7.txt'
    lines_seen=set()
    outfiile=open(writePath,'w+')
    f=open(readPath,'r')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)
    outfiile.close()
    f.close()


    count = 0
    #格式
    with open("Blackmatrix7.list","w") as fin:
        #for line in open("cnews.test2.txt"):
        file = open("Blackmatrix7.txt","r")
        for num1,line in enumerate(file):
            str=[]
            str = line
            str = str[0:str.find('/n')]
            if num1 < ctrl_1-1:
                continue
            fin.write(line)
        file.close()
        fin.close()

#######################################################################################



##########################################################################
#white过滤
    ctrl = 0
    ctrl_1 = 0
    file_1 = open("Advertising_1.list","w")

    while ctrl < static_white_num:
        whiteline = []
        whiteline = whiteListPro(ctrl)
        whiteline = whiteline[0:whiteline.find("\n")]
        #print(whiteline)
        for line in open("Advertising.txt"):
            str = []
            str = line
            
            if (str.find(whiteline) >= 0):
                #print(whiteline)
                #print(str)
                file_1.write(line)
                ctrl_1 += 1

        ctrl += 1
    print("adverti ctrl_1:",ctrl_1)
    file_1.close()

    #white hangshu 
    # static_white_num_3 =0
    # with open("Advertising_1.list", 'r') as f:
    #     static_white_num_3 = sum(1 for line in f)
    #     print('总行数为%s行。' % static_white_num_3)
    # f.close()


    with open("Advertising_1.list", 'a+') as f:
        for line in open("Advertising.txt"):
            f.write(line)
    f.close()

#white 去重
    readPath='Advertising_1.list'
    writePath='Advertising.txt'
    lines_seen=set()
    outfiile=open(writePath,'w+')
    f=open(readPath,'r')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)
    outfiile.close()
    f.close()


    count = 0
    #格式
    with open("Advertising.list","w") as fin:
        #for line in open("cnews.test2.txt"):
        file = open("Advertising.txt","r")
        for num1,line in enumerate(file):
            if num1 < ctrl_1-1:
                continue
            fin.write(line)
        file.close()
        fin.close()

#######################################################################################
   


    
    os.remove("1.txt")
    os.remove("11.txt")
    os.remove("7.txt")
    os.remove("77.txt")
    #os.remove("cnews.test2.txt")
    os.remove("WhiteList_1.txt")
    os.remove("whiteList1.txt")
    os.remove("Blackmatrix7.txt")
    os.remove("Advertising.txt")
    os.remove("Blackmatrix7_1.list")
    os.remove("Advertising_1.list")
    shutil.rmtree("__pycache__")
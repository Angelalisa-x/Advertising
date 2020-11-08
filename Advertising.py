# coding=utf-8

import csv, requests, re
import shutil
import os
import sys


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


# def whiteListPro(num):
#     file = open("WhiteList.txt","r")
#     for num1,line in enumerate(file):
#         if num1 == num:
#             #print("line:",line)
#             return line


'''
字符串查找函数，使用二分查找法在列表中进行查询
'''
def binarySearch(value, lines):
    right = len(lines) - 1
    left = 0
    a = value.strip()
    while left <= right:
        middle = int((right + left + 1)/2)
        b = lines[middle].strip()
        if a == b:
            return 1

        if a < b:
            right = middle - 1
        else:
            left = middle + 1

    return 0



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

    strWhite3 = []
    strWhite3 = WhiteList.pull3()

    strWhite4 = []
    strWhite4 = WhiteList.pull4()

    strWhite5 = []
    strWhite5 = WhiteList.pull5()

    strWhite6 = []
    strWhite6 = WhiteList.pull6()

    strWhite7 = []
    strWhite7 = WhiteList.pull7()


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


    #文本行数
    static_num = 0
    with open("7.txt", 'r') as f:
        static_num = sum(1 for line in f)
        print('总行数为%s行。' % static_num)
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
                if str in strWhite2:
                    count +=1
                    #print(str)
                    continue
                if str in strWhite3:
                    count +=1
                    continue
                if str in strWhite4:
                    count +=1
                    continue
                if str in strWhite5:
                    count +=1
                    continue
                if str in strWhite6:
                    count +=1
                    continue
                if str in strWhite7:
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
                    if str in strWhite4:
                        continue
                    if str in strWhite5:
                        continue
                    if str in strWhite6:
                        continue
                    if str in strWhite7:
                        continue

            str = "HOST-SUFFIX," + str
            str = str + ",REJECT" + "\n"
            fin.write(str)
        file.close()
        fin.close()

###############################################################################

############################################################################
#Advertising 进行处理
    print('count: %s' %count)
    file = open("11.txt","r")
    with open("Advertising.txt","w") as fin:
        for num1,value in enumerate(file):
            if(num1 >= static_num-count-2):
                if ".," in value:
                    continue
                if ".126.net" in value:
                    continue

                fin.write(value)
            #print("the nume:%s,the value is %s", static_num, value)
    file.close()
    fin.close()
#################################################################################

############################################################################
    #Blackmatrix7 进行处理
    with open("Blackmatrix7.list", 'w') as f:
        for line in open("7.txt"):
            f.write(line)
    f.close()
#############################################################################


#########################################################################################################

    fobj=open('exist.txt','w+')
    with open('whiteList.txt','r') as f:
        for line in f:
            with open('Advertising.txt','r') as obj:
                    for strs in obj:
                            if line.strip() in strs:
                                #print(line)
                                fobj.write(strs)
                                continue
    fobj.close()
    obj.close()

#######################################################################################################

################################################################################################################
#def file_qc():
    str1 = []
    file_1 = open("exist.txt","r",encoding="utf-8")
    for line in file_1.readlines():
        str1.append(line.replace("\n",""))

    str2 = []
    file_2 = open("Advertising.txt", "r", encoding="utf-8")
    for line in file_2.readlines():
        str2.append(line.replace("\n", ""))

    str_dump = []
    for line in str1:
        if line in str2:
            str_dump.append(line)    #将两个文件重复的内容取出来

    str_all = set(str1 + str2)      #将两个文件放到集合里，过滤掉重复内容

    for i in str_dump:              
        if i in str_all:
            str_all.remove(i)		#去掉重复的文件

    for str in str_all:             #去重后的结果写入文件
        #print(str)
        with open("QX.list","a+",encoding="utf-8") as f:
            f.write(str + "\n")


    file_1.close()
    file_2.close()

###############################################################################################################

#############################################################################################################
#Advertising 进行处理
    with open("Advertising.list", 'w') as f:
        for line in open("QX.list"):
            f.write(line)
    f.close()
###################################################################################################
    
    os.remove("1.txt")
    os.remove("11.txt")
    os.remove("7.txt")
    os.remove("cnews.test2.txt")
    os.remove("WhiteList_1.txt")
    os.remove("whiteList1.txt")
    os.remove("Advertising.txt")
    os.remove("QX.list")
    os.remove("exist.txt")
    shutil.rmtree("__pycache__")
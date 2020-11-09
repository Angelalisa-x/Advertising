# coding=utf-8

import csv, requests, re
import shutil
import os
import sys

static_Blackmatrix_num = 0  #Blackmatrix7行数

########################## 去重 #################################
def quchong(writePath,readPath):
    lines_seen=set()
    outfiile=open(writePath,'w+')
    f=open(readPath,'r')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)

    outfiile.close()
    f.close()

######################### 获取文件的行数 ########################
def getFileLineNum(fileName):
    with open(fileName, 'r') as f:
        line_num = sum(1 for line in f)
        print("%s: 总行数为%s: 行"%(fileName,line_num))
    f.close()
    return line_num

#################### pull Blackmatrix 规则，去掉前后缀 #############
def pullBlackmatrix7():
    url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list'
    #url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Advertising/Advertising.list'
    html = requests.get(url).text
    #print(html)
    with open("1.txt","w") as f:
        f.write(html)
    f.close()

    with open("blackmatrix7.txt","w+") as fin7:
        for line in open("1.txt"):
            if "#" in line:
                #print(line)
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "$" in line:
                continue
            if "。" in line:
                continue
            str=[]
            str = line
            str = str[str.find(',')+1: str.rfind(',')] + "\n"
            fin7.write(str)
    fin7.close()

########################### 切割文本文件 #################################
def qiegeFile(writePath,readPath,num):
    file = open(readPath,"r")
    fin = open(writePath,"w")
    for num1,line in enumerate(file):
        if num1 >= num:
            fin.write(line)
    file.close()
    fin.close()

########################## 合并文本文件 ##################################
def hebingFile(targetFile,mergeFile):
    fin = open(targetFile, "a+")
    for line in open(mergeFile,"r"):
        fin.write(line)
    fin.close()

########################## QX格式处理 ####################################
def geshiProcess(targetFile,readPath):
    fin = open(targetFile,"w")
    for line in open(readPath,"r"):
        str = []
        str = line
        str = str[0:str.find("\n")]
        str = "HOST-SUFFIX," + str + ",REJECT" + "\n"
        fin.write(str)
    fin.close()

############################ 自己整理的规则 ###############################
def pullEach():
            ###################### 梵 Start #########################
    url = 'https://raw.githubusercontent.com/Potterli20/filtering/master/purification'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","w+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()
            ################### 梵 End ########################

            ################## kbsmlDns Start ####################
    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        #for line in open("..\WhiteList\kbsmlDns.txt","r",encoding='UTF-8'):
        for line in open("WhiteList\kbsmlDns.txt","r",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                #print(line)
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if ":" in line:
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if "@@" in line:
                continue
            if "/" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "0.0.0.0" in line:
                str = str[str.find("0.0.0.0   ")+10:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()
            ############### kbsmlDns End ####################

            ################## GoodbyeAds Start ####################
    # url = 'https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-AdBlock-Filter.txt'
    # html = requests.get(url).text
    # with open("1.txt","w",encoding='UTF-8') as f:
    #     f.write(html)
    # f.close()

    # with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
    #     for line in open("1.txt",encoding='UTF-8'):
    #         str=[]
    #         str = line
    #         if "#" in line:
    #             continue
    #         if "!" in line:
    #             continue
    #         if line == '\n':
    #             continue
    #         if "。" in line:
    #             continue
    #         if "@" in line:
    #             continue
    #         if ":" in line:
    #             continue
    #         if "||*." in line:
    #             str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||." in line:
    #             str = str[str.find("||.")+3:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||*" in line:
    #             str = str[str.find("||*")+3:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||" in line:
    #             str = str[str.find("||")+2:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "$" in line:
    #             continue
    #         fin7.write(str)
    # fin7.close()
            ################## GoodbyeAds End ####################

            ################## AdGuardDNS Start ####################
    url = 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()
            ################## AdGuardDNS End ####################

            ################## 1Hosts-Pro Start ###################
    url = 'https://badmojr.github.io/1Hosts/Pro/adblock.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()            
            ################## 1Hosts-Pro End #####################
          

###################### 执行函数 Start ########################
def doProcessCustomRuleAD():
    pullBlackmatrix7()
    pullEach()


    quchong("KnightAD_1.txt","KnightAD.txt")
    quchong("blackmatrix7_1.txt","blackmatrix7.txt")
    blackmatrix7_num = getFileLineNum("blackmatrix7_1.txt")

    hebingFile("blackmatrix7_1.txt","KnightAD_1.txt")
    quchong("blackmatrix7_2.txt","blackmatrix7_1.txt")

    qiegeFile("KnightAD_2.txt","blackmatrix7_2.txt",blackmatrix7_num)

    geshiProcess("KnightAD.list","KnightAD_2.txt")


    os.remove("1.txt")
    os.remove("blackmatrix7.txt")
    os.remove("blackmatrix7_1.txt")
    os.remove("blackmatrix7_2.txt")
    os.remove("KnightAD.txt")
    os.remove("KnightAD_1.txt")
    os.remove("KnightAD_2.txt") 
###################### 执行函数 End ########################

# if __name__ == '__main__':
    # pullBlackmatrix7()
    # pullEach()


    # quchong("KnightAD_1.txt","KnightAD.txt")
    # quchong("blackmatrix7_1.txt","blackmatrix7.txt")
    # blackmatrix7_num = getFileLineNum("blackmatrix7_1.txt")

    # hebingFile("blackmatrix7_1.txt","KnightAD_1.txt")
    # quchong("blackmatrix7_2.txt","blackmatrix7_1.txt")

    # qiegeFile("KnightAD_2.txt","blackmatrix7_2.txt",blackmatrix7_num)

    # geshiProcess("KnightAD.list","KnightAD_2.txt")


    # os.remove("1.txt")
    # os.remove("blackmatrix7.txt")
    # os.remove("blackmatrix7_1.txt")
    # os.remove("blackmatrix7_2.txt")
    # os.remove("KnightAD.txt")
    # os.remove("KnightAD_1.txt")
    # os.remove("KnightAD_2.txt")

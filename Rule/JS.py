import csv, requests, re
import shutil
import os
import sys


def addWhite(targetFile,readPath):
    fin = open(targetFile,"w",encoding='UTF-8')
    for line in open(readPath,"r",encoding='UTF-8'):
        if "music.126.net" in line:
            continue
######### yudong white #############
        if ",lianmeng," in line:
            continue
        if ",analytics," in line:
            continue
        if ",aliapp.org," in line:
            continue
        str=[]
        str = line
        str = str[0:str.find('/n')]
        if "meituan.net" == str:
            continue
        if "meituan.com" == str:
            continue
        if "analytics" == str:
            continue
        fin.write(line)
    fin.close()

################# 格式处理，方便去重 ############
def geshiProcess(targetFile,readPath):
    with open(targetFile,"w",encoding='UTF-8') as fin7:
        for line in open(readPath,encoding='UTF-8'):
            str = []
            str = line
            if "0.0.0.0   " in line:
                str = str[10:str.find("\n")]
                str = "127.0.0.1 " + str + "\n"
                fin7.write(str)
                continue
            if "0.0.0.0  " in line:
                str = str[9:str.find("\n")]
                str = "127.0.0.1 " + str + "\n"
                fin7.write(str)
                continue
            if "0.0.0.0 " in line:
                str = str[8:str.find("\n")]
                str = "127.0.0.1 " + str +"\n"
                fin7.write(str)
                continue

            fin7.write(line)
        fin7.close()

def Deduplication(writePath,readPath):
    lines_seen=set()
    outfiile=open(writePath,'w+',encoding='UTF-8')
    f=open(readPath,'r',encoding='UTF-8')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)

    outfiile.close()
    f.close()

def pullTaskWangzhanInfo(urlInfo):
    url = urlInfo
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("TaskJS.txt","a+",encoding='UTF-8') as fin7:
        fin7.write("\n")
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            strL = []
            strR = []
            str = line
            #str = str[0:str.find("\n")]
            if "script-path" in line:
                dier = str.find('\"',len(str[0:str.find('\"')])+1)
                strL = str[str.find('\"')+1:dier]
                strR = str[dier+14:str.find("\n")]
                str = strL + " " + strR + ", enabled=true" + "\n"
                fin7.write(str)
                continue
            
            fin7.write(line)
        fin7.close()

def pullWangzhandizhi(urlInfo):
    url = urlInfo
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("Wangzhandizhi.txt","a+",encoding='UTF-8') as fin7:
        fin7.write("\n")
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            strL = []
            strR = []
            str = line
            if "</a></span>" in line:
                str = str[str.find("href=\"") + 6 : str.find("\n")]
                if ".js" in line:
                    str = str[0 : str.find(".js") + 3] + "\n"
                    strL = str[0 : str.find("blob")]
                    strR = str[str.find("blob") + 5 : str.find("\n")] + "\n"
                    str =  "https://raw.githubusercontent.com" + strL + strR
                    fin7.write(str)
                    continue
            
            
        fin7.close()

def pullWangzhangGitee(urlInfo):
    url = urlInfo
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("Wangzhandizhi.txt","a+",encoding='UTF-8') as fin7:
        fin7.write("\n")
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            strL = []
            strR = []
            str = line
            if "<a href=" in line:
                str = str[str.find("href=\"") + 6 : str.find("\n")]
                if "不要fork-请点亮star" in line:
                    continue
                if ".js" in line:
                    str = str[0 : str.find(".js") + 3] + "\n"
                    strL = str[0 : str.find("blob")] + "raw/"
                    strR = str[str.find("blob") + 5 : str.find("\n")] + "\n"
                    str =  "https://gitee.com" + strL + strR
                    fin7.write(str)
                    continue
            
            
        fin7.close()

def pullJS(urlInfo):
    url = urlInfo
    html = requests.get(url).text

    fin = open("JS.txt","a",encoding='UTF-8')
    fin.write(html)
    fin.close()

def pullios7(urlInfo, txt):
    url = urlInfo
    html = requests.get(url).text

    fin = open(txt,"w+",encoding='UTF-8')
    fin.write(html)
    fin.close()

################ 合并文件 #################
def hebingFile(targetFile,mergeFile):
    fin = open(targetFile, "a+",encoding='UTF-8')
    for line in open(mergeFile,"r",encoding='UTF-8'):
        fin.write(line)
    fin.close()

if __name__ == "__main__":

    fin = open("TaskJS.txt","w",encoding='UTF-8')
    fin.close()
    pullTaskWangzhanInfo('https://raw.githubusercontent.com/Tartarus2014/Loon-Script/master/Task.conf')
    pullTaskWangzhanInfo('https://raw.githubusercontent.com/Tartarus2014/Surge-Script/master/Task.sgmodule')

    Deduplication("TaskJS.conf","TaskJS.txt")

    fin = open("Wangzhandizhi.txt","w",encoding='UTF-8')
    fin.close()
    # pullWangzhandizhi('https://github.com/lxk0301/jd_scripts/tree/master')
    # pullWangzhandizhi('https://github.com/799953468/Quantumult-X/tree/master/Scripts/JD')
    # pullWangzhandizhi('https://github.com/whyour/hundun/tree/master/quanx')
    # pullWangzhandizhi('https://github.com/MoPoQAQ/Script/tree/main/Me')
    # pullWangzhandizhi('https://github.com/LXK9301/jd_scripts/tree/master')
    pullWangzhandizhi('https://github.com/zero205/JD_tencent_scf/tree/main')
    pullWangzhandizhi('https://github.com/Ariszy/Private-Script/tree/master/JD')
    pullWangzhandizhi('https://github.com/star261/jd/tree/main/scripts')
    pullWangzhandizhi('https://github.com/yangtingxiao/QuantumultX/tree/master/scripts/jd')
    pullWangzhandizhi('https://github.com/JDHelloWorld/jd_scripts')

    fin = open("JS.txt","w",encoding='UTF-8')
    fin.close()
    # pullJS('https://raw.githubusercontent.com/royximei/QuantumultX/master/js.conf')
    # pullJS('https://raw.githubusercontent.com/id77/QuantumultX/master/rewrite/other.conf')
    # pullJS('https://raw.githubusercontent.com/id77/QuantumultX/master/rewrite/ad.conf')
    # pullJS('https://raw.githubusercontent.com/id77/QuantumultX/master/rewrite/vip.conf')
    # pullJS('https://raw.githubusercontent.com/ddgksf2013/Cuttlefish/master/Rewrite/Quan_crack.conf')
    # pullJS('https://raw.githubusercontent.com/ddgksf2013/Cuttlefish/master/Rewrite/Ua.conf')
    # pullJS('https://raw.githubusercontent.com/ddgksf2013/Cuttlefish/master/Rewrite/Xxys.conf')
    # pullJS('https://raw.githubusercontent.com/ddgksf2013/Cuttlefish/master/Rewrite/Youtube.conf')
    # pullJS('https://raw.githubusercontent.com/ddgksf2013/Cuttlefish/master/Rewrite/Crazyjoy.conf')
    # pullJS('https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/Js.conf')
    # Deduplication("JS-Ex.txt", "JS.txt")
    pullJS('https://raw.githubusercontent.com/zero205/JD_tencent_scf/main/jd_task.json')
    Deduplication("JS.json", "JS.txt")

    #pullWangzhangGitee('https://gitee.com/lxk0301/jd_scripts/tree/master')

    pullios7('https://anti-ad.net/surge2.txt',
                'Surge/surge2.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/Surge/AllInOne/AllInOne.sgmodule',
                'Surge/SurgeAllInOne.sgmodule')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingTest/AdvertisingTest.list',
                'Surge/AdvertisingTest.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingTest/AdvertisingTest_Domain.list',
                'Surge/AdvertisingTest_Domain.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/360/360.list',
                'Surge/360.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/SystemOTA/SystemOTA.list',
                'Surge/SystemOTA.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list',
                'Surge/YouTube.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list',
                'Surge/Telegram.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/China/China.list',
                'Surge/China.list')
    pullios7('https://raw.githubusercontent.com/asnfohsdgfbkxcv/script/main/Task%20JD.sgmodule',
                'Surge/TaskJD.sgmodule')
    

    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/Loon/AllInOne/AllInOne.plugin',
                'Loon/LoonAllInOne.plugin')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/AdvertisingTest/AdvertisingTest.list',
                'Loon/AdvertisingTest.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/AdvertisingTest/AdvertisingTest_Domain.list',
                'Loon/AdvertisingTest_Domain.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/360/360.list',
                'Loon/360.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/SystemOTA/SystemOTA.list',
                'Loon/SystemOTA.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/YouTube/YouTube.list',
                'Loon/YouTube.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Telegram/Telegram.list',
                'Loon/Telegram.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/China/China.list',
                'Loon/China.list')


    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rewrite/QuantumultX/AllInOne/AllInOne.conf',
                'QuantumultX/AllInOne.conf')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list',
                'QuantumultX/AdvertisingTest.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/360/360.list',
                'QuantumultX/360.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/SystemOTA/SystemOTA.list',
                'QuantumultX/SystemOTA.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/YouTube/YouTube.list',
                'QuantumultX/YouTube.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Telegram/Telegram.list',
                'QuantumultX/Telegram.list')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/China/China.list',
                'QuantumultX/China.list')
    pullios7('https://raw.githubusercontent.com/sngxpro/QuanX/master/task/AllinOne.json',
                'QuantumultX/sngxproTaskAllinOne.json')
    pullios7('https://raw.githubusercontent.com/sngxpro/QuanX/master/rewrite/cookie.conf',
                'QuantumultX/sngxproCookie.conf')


    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AdvertisingTest/AdvertisingTest.yaml',
                'Clash/AdvertisingTest.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AdvertisingTest/AdvertisingTest_Domain.yaml',
                'Clash/AdvertisingTest_Domain.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/360/360.yaml',
                'Clash/360.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/SystemOTA/SystemOTA.yaml',
                'Clash/SystemOTA.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml',
                'Clash/YouTube.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml',
                'Clash/Telegram.yaml')
    pullios7('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/China/China.yaml',
                'Clash/China.yaml')

    pullios7('https://qxnav.com/rules/QuantumultX/gz/guanggao.list','guanggao.list')

    pullios7('https://qxnav.com/rules/QuantumultX/qixin.json','qixin.json')

    pullios7('https://cdn.jsdelivr.net/gh/sngxpro3/QuanxTask@main/JDTask/JDTask.json', 'sngxpro3JDTask.json')

    pullios7('https://cdn.jsdelivr.net/gh/sngxpro3/QuanxTask@main/OtherThanJD/OthersThanJD.json', 'sngxpro3OtherTask.json')


    os.remove("TaskJS.txt")
    os.remove("temporary.txt")
    os.remove("JS.txt")
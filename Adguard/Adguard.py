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

def pullWangzhanInfo(urlInfo):
    url = urlInfo
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        fin7.write("\n")
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if "#" in line:
                continue
            if "@@||" in line:
                continue
            if "localhost" in line:
                continue
            fin7.write(line)
        fin7.close()

def pullKbsml():
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt '

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        fin7.write("\n")
        for line in open("kbsm.txt",encoding='UTF-8'):
            if "!" in line:
                continue
            if "#" in line:
                continue
            if "@@||" in line:
                continue
            fin7.write(line)
        fin7.close()

def pullKbsmlDns():
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall-dns.txt'

    with open("Adguard.txt","w",encoding='UTF-8') as fin7:
        for line in open("../WhiteList/kbsmlDns.txt",encoding='UTF-8'):
            if "!" in line:
                continue
            if "#" in line:
                continue
            if "@@||" in line:
                continue
            fin7.write(line)
        fin7.close()

def pullBlackmatrix7():
    url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("blackmatrix7.txt","w",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            dier = str.find(',',len(str[0:str.find(',')])+1)
            if "!" in line:
                continue
            if "#" in line:
                continue
            if "," in line:
                str = str[str.find(',')+1:dier]
                if "HOST-KEYWORD," in line:
                    str = "||" + str + "^" + "\n"
                    fin7.write(str)
                    continue
                if "HOST-SUFFIX," in line:
                    str = "||" + str + "^" + "\n"
                    fin7.write(str)
                    continue
                if "HOST," in line:
                    str = "127.0.0.1 " + str + "\n"
                    fin7.write(str)
                    continue
                if "IP-CIDR" in line:
                    continue
        fin7.close()

################ 合并文件 #################
def hebingFile(targetFile,mergeFile):
    fin = open(targetFile, "a+",encoding='UTF-8')
    for line in open(mergeFile,"r",encoding='UTF-8'):
        fin.write(line)
    fin.close()

if __name__ == "__main__":

    pullKbsmlDns()
    pullKbsml()
    pullWangzhanInfo('https://anti-ad.net/easylist.txt')
    pullWangzhanInfo('https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt')
    pullWangzhanInfo('https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt')
    pullWangzhanInfo('https://gitee.com/lhzgl6587/hosts/raw/master/myruler')
    pullWangzhanInfo('https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts')
    pullWangzhanInfo('https://gitee.com/anye1998/Adguard-List-of-personal-rules/raw/master/List-of-personal-rules.txt')
    pullWangzhanInfo('https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt')
    pullWangzhanInfo('https://raw.githubusercontent.com/DivineEngine/AdGuardFilter/master/filter.txt')
    pullWangzhanInfo('https://raw.githubusercontent.com/neodevpro/neodevhost/master/host')
    pullWangzhanInfo('https://raw.githubusercontent.com/Potterli20/filtering/master/purification')
    pullWangzhanInfo('https://adaway.org/hosts.txt')
    pullWangzhanInfo('https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts')
    pullWangzhanInfo('https://raw.githubusercontent.com/Goooler/1024_hosts/master/hosts')

    

    Deduplication("Adguard_1.txt","Adguard.txt")
    addWhite("AdguardEx.txt","Adguard_1.txt")

    geshiProcess("AdguardEx_1.txt","AdguardEx.txt")
    Deduplication("AdguardEx.txt","AdguardEx_1.txt")

    pullBlackmatrix7()
    hebingFile("blackmatrix7.txt","AdguardEx.txt")
    Deduplication("AdguardEx_1.txt","blackmatrix7.txt")
    addWhite("AdguardEx.txt","AdguardEx_1.txt")


    os.remove("temporary.txt")
    os.remove("Adguard.txt")
    os.remove("Adguard_1.txt")
    os.remove("AdguardEx_1.txt")
    os.remove("blackmatrix7.txt")


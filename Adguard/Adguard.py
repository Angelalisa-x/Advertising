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

def pull():
    ################# anti-ad #################
    url = 'https://anti-ad.net/easylist.txt'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("Adguard.txt","w",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            fin7.write(str)
        fin7.close()

    ############## Adgk ##############
    url = 'https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            fin7.write(str)
        fin7.close()

    ####################    kbsml  ############
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt '

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("kbsm.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            fin7.write(str)
        fin7.close()

    ##################  lhzgl6587   ###############
    url = 'https://gitee.com/lhzgl6587/hosts/raw/master/myruler '
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            fin7.write(str)
        fin7.close()

    ##################  jdlingyu   ###############
    url = 'https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if "127.0.0.1 " in line:
                str = str[str.find("127.0.0.1 ")+10:str.find("\n")]
                str = "||" + str + "^" + "\n"
                fin7.write(str)
        fin7.close()

    ##################  neodevpro  ###############
    url = 'https://raw.githubusercontent.com/neodevpro/neodevhost/master/host'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if "0.0.0.0  " in line:
                str = str[str.find("0.0.0.0  ")+9:str.find("\n")]
                str = "||" + str + "^" + "\n"
                fin7.write(str)
        fin7.close()

    ##################  AdAway  ###############
    url = 'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "localhost" in line:
                continue
            if "127.0.0.1 " in line:
                str = str[str.find("127.0.0.1 ")+10:str.find("\n")]
                str = "||" + str + "^" + "\n"
                fin7.write(str)
        fin7.close()   

def PullDirectly():

    ################## anti-ad ##########################
    url = 'https://anti-ad.net/easylist.txt'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","w",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "@@||" in line:
                continue
            fin7.write(str)
        fin7.close()

    ####################   kbsml  ############
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt '

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("kbsm.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "@@||" in line:
                continue
            fin7.write(str)
        fin7.close()

    #################### kbsml DNS ############
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall-dns.txt'

    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("../WhiteList/kbsmlDns.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "@@||" in line:
                continue
            fin7.write(str)
        fin7.close()

    ##################### AdAway ###################
    url = 'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt'
    html = requests.get(url).text

    fin = open("temporary.txt","w",encoding='UTF-8')
    fin.write(html)
    fin.close()
 
    with open("Adguard.txt","a+",encoding='UTF-8') as fin7:
        for line in open("temporary.txt",encoding='UTF-8'):
            str = []
            str = line
            str = str[0:str.find("\n")] + "\n"
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "@@||" in line:
                continue
            fin7.write(str)
        fin7.close()

if __name__ == "__main__":
    #pull()
    PullDirectly()

    Deduplication("Adguard_1.txt","Adguard.txt")
    addWhite("AdguardEx.txt","Adguard_1.txt")


    os.remove("temporary.txt")
    os.remove("Adguard.txt")
    os.remove("Adguard_1.txt")


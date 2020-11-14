import csv, requests, re
import shutil
import os
import sys


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

    ####################    wp-content  ############
    url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt '
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
            fin7.write(str)
        fin7.close()


if __name__ == "__main__":
    pull()

    Deduplication("AdguardEx.txt","Adguard.txt")


    os.remove("temporary.txt")
    os.remove("Adguard.txt")







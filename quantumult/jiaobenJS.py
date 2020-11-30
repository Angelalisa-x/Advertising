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

    #Deduplication("TaskJS.conf","TaskJS.txt")

    fin = open("Wangzhandizhi.txt","w",encoding='UTF-8')
    fin.close()
    pullWangzhandizhi('https://github.com/lxk0301/jd_scripts/tree/master')
    pullWangzhandizhi('https://github.com/799953468/Quantumult-X/tree/master/Scripts/JD')
    pullWangzhandizhi('https://github.com/yangtingxiao/QuantumultX/tree/master/scripts/jd')

    


    os.remove("temporary.txt")
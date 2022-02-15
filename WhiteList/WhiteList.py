
import requests, re, os
import shutil

##################### 去重 ###############################
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

######################### 格式处理 #############################
def geshiProcess_Qx(targetFile,readPath):
    f = open(targetFile,"w+")
    for line in open(readPath,"r"):
        str = []
        str = line
        str = str[0:str.find("\n")]
        str = "HOST-SUFFIX," + str + ",DIRECT" + "\n"
        f.write(str)
    f.close()

def geshiProcess_Surge(targetFile,readPath):
    f = open(targetFile,"w+")
    for line in open(readPath,"r"):
        str = []
        str = line
        str = str[0:str.find("\n")]
        str = "DOMAIN-SUFFIX," + str + "\n"
        f.write(str)
    f.close()

######################## 去除一些白名单 ############################
def unwantedWhitelist(targetFile,readPath):
    fin = open(targetFile,"w")
    for line in open(readPath,"r"):
        # if ",lianmeng," in line:
        #     continue
        str=[]
        str = line
        str = str[0:str.find('/n')]
        if "snssdk.com" == str:
            continue
        if ".snssdk.com" == str:
            continue
        if "*snssdk.com" == str:
            continue
        fin.write(line)
    fin.close() 

######################## pull whitelist #####################################
                ############# Potterli20 Start ###################
def pullWhite():
    url = 'https://trli.coding.net/p/file/d/file/git/raw/master/ad-allow.txt'
    html = requests.get(url).text
    with open("whiteList1.txt","w") as f:
        f.write(html)
    f.close()

    fwhite=open("whiteList_1.txt","w")
    for line in open("whiteList1.txt"):
        if "#" in line:
            #print(line)
            continue
        if "!" in line:
            continue
        if line in ['\n','\r\n']:
            continue
        if line.strip() == "":
            continue
        str=[]
        str = line
        if "@@||*" in line:
            if "^" in line:
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||" in line:
            if "^" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||*." in line:
            if "^" in line:
                str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||." in line:
            if "^" in line:
                str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
    fwhite.close()
            ############# Potterli20 End ###################

            ############# liwenjie119 Start ################
    # url = 'https://raw.githubusercontent.com/liwenjie119/adg-rules/master/white.txt'
    # html = requests.get(url).text
    # #print(html)
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         #print(line)
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str=[]
    #     str = line
    #     if "@@||*" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||*." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    # fwhite.close()
            ############# liwenjie119 End ################

            ############# AdGuardDNSPassList Start ################
    # url = 'https://raw.githubusercontent.com/etotakeo/AdGuardDNSPassList/master/DNS-Pass-List'
    # html = requests.get(url).text
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         #print(line)
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str=[]
    #     str = line
    #     if "@@||*" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||*." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    # fwhite.close()
            ############# AdGuardDNSPassList End   ################

            ############# kbsml Start  ################
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall-dns.txt'
    #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt'

    fwhite=open("whiteList_1.txt","a+")
    for line in open("kbsmlDns.txt",encoding='UTF-8'):
    #for line in open("WhiteList\kbsmlDns.txt",encoding='UTF-8'):
        str=[]
        str = line
        if "@@||*" in line:
            if "^" in line:
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||" in line:
            if "^" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||*." in line:
            if "^" in line:
                str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        if "@@||." in line:
            if "^" in line:
                str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
    fwhite.close()
            ############ adg-kall ############
    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("..\Adguard\kbsm.txt",encoding='UTF-8'):
    #     str=[]
    #     str = line
    #     if "$" in line:
    #         continue
    #     if "*" in line:
    #         continue
    #     if "@@||*" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||*." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    # fwhite.close()
            ############# kbsml End    ################

            ############# anti-ad Star   ################
    # url = 'https://anti-ad.net/easylist.txt'
    # html = requests.get(url).text
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         #print(line)
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str=[]
    #     str = line
    #     if "@@||*" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||*." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    # fwhite.close()
            ############# anti-ad End    ################

           ############# lhzgl6587 Star   ################
    # url = 'https://gitee.com/lhzgl6587/hosts/raw/master/myruler'
    # html = requests.get(url).text
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         #print(line)
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str=[]
    #     str = line
    #     if "@@||*" in line:
    #         str = str[str.find("@@||*")+5:str.rfind("\n")] + "\n"
    #         fwhite.write(str)
    #         continue
    #     if "@@||" in line:
    #         str = str[str.find("@@||")+4:str.rfind("\n")] + "\n"
    #         fwhite.write(str)
    #         continue
    #     if "@@||*." in line:
    #         str = str[str.find("@@||*.")+6:str.rfind("\n")] + "\n"
    #         fwhite.write(str)
    #         continue
    #     if "@@||." in line:
    #         str = str[str.find("@@||.")+5:str.rfind("\n")] + "\n"
    #         fwhite.write(str)
    #         continue
    # fwhite.close()
            ############# lhzgl6587 End    ################

            ############# DivineEngine Star   ################
    # url = 'https://raw.githubusercontent.com/DivineEngine/AdGuardFilter/master/filter.txt'
    # html = requests.get(url).text
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         #print(line)
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str=[]
    #     str = line
    #     if "@@||*" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||" in line:
    #         if "^" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||*." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||*.")+6:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     if "@@||." in line:
    #         if "^" in line:
    #             str = str[str.find("@@||.")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    # fwhite.close()
            ############# DivineEngine End    ################

            ############# blackmatrix7 Star ###################
    # url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/WhiteList/WhiteList.list'
    # html = requests.get(url).text
    # with open("whiteList1.txt","w") as f:
    #     f.write(html)
    # f.close()

    # fwhite=open("whiteList_1.txt","a+")
    # for line in open("whiteList1.txt"):
    #     if "#" in line:
    #         continue
    #     if "!" in line:
    #         continue
    #     if line in ['\n','\r\n']:
    #         continue
    #     if line.strip() == "":
    #         continue
    #     str = []
    #     str = line
    #     dier = str.find(',',len(str[0:str.find(',')])+1)
    #     str = str[str.find(',')+1:dier] + "\n"
    #     fwhite.write(str)
    # fwhite.close()
            ############# blackmatrix7 End ###################
 
if __name__ == '__main__':
    pullWhite()

    quchong("whiteList_2.txt","whiteList_1.txt")
    unwantedWhitelist("swhiteList.txt","whiteList_2.txt")
    geshiProcess_Qx("whiteList_Qx.list", "swhiteList.txt")
    geshiProcess_Surge("whiteList_Surge.list", "swhiteList.txt")


    os.remove("whiteList1.txt")
    os.remove("whiteList_1.txt")
    os.remove("whiteList_2.txt")
    #shutil.rmtree("__pycache__")




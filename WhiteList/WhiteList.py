
import requests, re, os
import shutil


class whiteList:
    #去重
    def quchong(readPath,writePath):
        # readPath='whiteList_1.txt'
        # writePath='whiteList.list'
        lines_seen=set()
        outfiile=open(writePath,'w+')
        f=open(readPath,'r')
        for line in f:
            if line not in lines_seen:
                outfiile.write(line)
                lines_seen.add(line)

        outfiile.close()
        f.close()

    #格式处理
    def geshiProcess():
        f = open("whiteList.list","w+")
        for line in open("whiteList.txt","r"):
            str = []
            str = line
            str = str[0:str.find("\n")]
            str = "HOST-SUFFIX," + str + ",DIRECT" + "\n"
            f.write(str)
        f.close()

    def pull2():
        url = 'https://raw.githubusercontent.com/Potterli20/filtering/master/filtering.txt'
        html = requests.get(url).text
        #print(html)
        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("whiteList_1.txt","a+")
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
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
            if "@@||" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        fwhite.close()
        return html
    
    def pull3():
        url = 'https://raw.githubusercontent.com/liwenjie119/adg-rules/master/white.txt'
        html = requests.get(url).text
        #print(html)
        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("whiteList_1.txt","a+")
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
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
            if "@@||" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        fwhite.close()
        return html
    
    def pull7():
        url = 'https://raw.githubusercontent.com/etotakeo/AdGuardDNSPassList/master/DNS-Pass-List'
        html = requests.get(url).text
        #print(html)
        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("whiteList_1.txt","a+")
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
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
            if "@@||" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        fwhite.close()
        return html

    def pullkbsml():
        #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall-dns.txt'
        #url = 'https://www.kbsml.com/wp-content/uploads/adblock/adguard/adg-kall.txt'

        fwhite=open("whiteList_1.txt","a+")
        for line in open("kbsmlDns.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "@@||*" in line:
                str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
            if "@@||" in line:
                str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
                fwhite.write(str)
                continue
        fwhite.close()

    # def pullADgk():
    #     url = 'https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt'
    #     html = requests.get(url).text
    #     with open("whiteList1.txt","w",encoding='UTF-8') as f:
    #         f.write(html)
    #     f.close()

    #     fwhite=open("whiteList_1.txt","w")
    #     for line in open("whiteList1.txt",encoding='UTF-8'):
    #         str=[]
    #         str = line
    #         if "#" in line:
    #             #print(line)
    #             continue
    #         if "!" in line:
    #             continue
    #         if "$" in line:
    #             continue
    #         if "=" in line:
    #             continue
    #         if "?" in line:
    #             continue
    #         if "/|" in line:
    #             continue
    #         if "/" in line:
    #             continue
    #         if "。" in line:
    #             continue
    #         if "@@||*" in line:
    #             str = str[str.find("@@||*")+5:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #         if "@@||" in line:
    #             str = str[str.find("@@||")+4:str.rfind("^")] + "\n"
    #             fwhite.write(str)
    #             continue
    #     fwhite.close()    
 

if __name__ == '__main__':
    whiteList.pull2()
    whiteList.pull3()
    whiteList.pull7()
    whiteList.pullkbsml()
    # whiteList.pullADgk()


    whiteList.quchong("whiteList_1.txt","whiteList.txt")
    whiteList.geshiProcess()



    os.remove("whiteList1.txt")
    os.remove("whiteList_1.txt")
    #shutil.rmtree("__pycache__")




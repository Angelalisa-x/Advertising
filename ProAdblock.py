#https://badmojr.github.io/1Hosts/Pro/adblock.txt


import requests, re
import shutil

from bs4 import BeautifulSoup

class ProAdblock:

    def pull():
        url = 'https://badmojr.github.io/1Hosts/Pro/adblock.txt'
        html = requests.get(url).text
        #print(html)
        with open("1.txt","w") as f:
            f.write(html)
        f.close()

        with open("11.txt","a+") as fin:
            fwhite=open("WhiteList_1.txt","a+")
            for line in open("1.txt"):
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
                if "#" in line:
                    #print(line)
                    continue
                if "!" in line:
                    continue
                if "@" in line:
                    continue
                if "*" in line:
                    continue
                if "//" in line:
                    continue
                if "/" in line:
                    continue
                if "$" in line:
                    continue
                if "。" in line:
                    continue
                if line in ['\n','\r\n']:
                    continue
                if line.strip() == "":
                    continue
                line = line.split("||")[1]
                
                str=[]
                str = line
    
                str = str[0:str.find('^')] + "\n"
                #str = "HOST," + str
                #str = str + ",Advertising" + "\n"
                fin.write(str)
                
        fin.close()
        fwhite.close()
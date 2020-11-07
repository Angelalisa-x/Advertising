#https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts


import requests, re
import shutil

from bs4 import BeautifulSoup

class jdlingyu:

    def pull():
        url = 'https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts'
        html = requests.get(url).text
        #print(html)
        with open("1.txt","w") as f:
            f.write(html)
        f.close()

        with open("11.txt","a+") as fin:
            fwhite=open("WhiteList_1.txt","a+")
            for line in open("1.txt"):
                if "@@||" in line:
                    fwhite.write(line)
                if "#" in line:
                    #print(line)
                    continue
                if "::" in line:
                    continue
                if "<" in line:
                    continue
                if ">" in line:
                    continue
                if "!" in line:
                    continue
                if "localhost" in line:
                    continue
                if "ip6" in line:
                    continue
                if "@" in line:
                    continue
                if "*" in line:
                    continue
                if "/" in line:
                    continue
                if "//" in line:
                    continue
                if "$" in line:
                    continue
                if "。" in line:
                    continue
                if line in ['\n','\r\n']:
                    continue
                if line.strip() == "":
                    continue

                
                str=[]
                str = line
    
                str = str[str.find('127.0.0.1 ')+10:str.find('/')] + "\n"
                #str = "HOST," + str
                #str = str + ",Advertising" + "\n"
                fin.write(str)
                
        fin.close()
        fwhite.close()
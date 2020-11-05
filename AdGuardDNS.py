#https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt

import requests, re
import shutil

from bs4 import BeautifulSoup

class AdGuardDNS:

    def pull():
        url = 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
        html = requests.get(url).text
        #print(html)
        with open("1.txt","w") as f:
            f.write(html)
        f.close()

        with open("11.txt","a+") as fin:
            for line in open("1.txt"):
                if "#" in line:
                    #print(line)
                    continue
                if "!" in line:
                    continue
                if "*" in line:
                    continue
                if line in ['\n','\r\n']:
                    continue
                if line.strip() == "":
                    continue
                if "@" in line:
                    continue
                if "//" in line:
                    continue
                #line = line.split(",")[1]
                
                str=[]
                str = line
                str = str[str.find('||')+2: str.rfind('^')] + "\n"
    
                #str = str[0:str.find(',')] + "\n"
                #str = "HOST," + str
                #str = str + ",Advertising" + "\n"
                fin.write(str)
                
        fin.close()
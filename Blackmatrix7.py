#https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list

import requests, re
import shutil

from bs4 import BeautifulSoup

class Blackmatrix7:

    def pull():
        url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list'
        html = requests.get(url).text
        #print(html)
        with open("1.txt","w") as f:
            f.write(html)
        f.close()

        with open("77.txt","w") as f:
            f.write(html)
        f.close

        with open("7.txt","w+") as fin7:
            with open("11.txt","w+") as fin:
                for line in open("1.txt"):
                    if "#" in line:
                        #print(line)
                        continue
                    if "!" in line:
                        continue
                    if line in ['\n','\r\n']:
                        continue
                    if line.strip() == "":
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
                    #line = line.split(",")[1]
                    
                    str=[]
                    str = line
                    str = str[str.find(',')+1: str.rfind(',')] + "\n"
        
                    #str = str[0:str.find(',')] + "\n"
                    #str = "HOST," + str
                    #str = str + ",Advertising" + "\n"
                    fin.write(str)
                    fin7.write(str)
                
        fin.close()
        fin7.close()
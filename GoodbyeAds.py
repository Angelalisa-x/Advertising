# coding=utf-8

#https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-AdBlock-Filter.txt


import csv, requests, re
import shutil

from bs4 import BeautifulSoup

class GoodbyeAds:

    def pull():
        url = 'https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-AdBlock-Filter.txt'
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
                if "@" in line:
                    continue
                if "*" in line:
                    continue
                if line in ['\n','\r\n']:
                    continue
                if "/" in line:
                    continue
                if "//" in line:
                    continue
                if "$" in line:
                    continue
                if line.strip() == "":
                    continue
                if "。" in line:
                    continue
                line = line.split("||")[1]
                
                str=[]
                str = line
    
                str = str[0:str.find('^')] + "\n"
                #str = "HOST," + str
                #str = str + ",Advertising" + "\n"
                fin.write(str)
                
        fin.close()


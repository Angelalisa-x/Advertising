import csv, requests, re
import shutil
import os
import sys


def pullios7(urlInfo, list):
    url = urlInfo
    html = requests.get(url).text

    fin = open("1.txt", "w+", encoding='UTF-8')
    fin.write(html)
    fin.close()

    with open("2.txt","w+", encoding='UTF-8') as fin2:
        for line in open("1.txt", encoding='UTF-8'):
            str = []
            str = line
            if "js-navigation-open Link--primary" in line and "css-truncate css-truncate-target d-block width-fit" in line:
                str = str[str.find("href=\"") + 6 : str.find("\n")]
                if "\">" in str:
                    str = str[0 : str.find("\">")] + "\n"
                    if "README.md" in str:
                        strL = str[0 : str.find("blob")]
                        strR = str[str.find("blob") + 5 : str.find("\n")]
                        str =  "https://raw.githubusercontent.com" + strL + strR
                        #print(str)
                        html = requests.get(str).text
                        #print(html)
                        
                        folderRe = os.getcwd() +  "\\" + list
                        if not os.path.exists(folderRe):
                            os.makedirs(folderRe)
                        Readme = folderRe + "\\" + "README.md"
                        finRE = open(Readme, "w+", encoding='UTF-8')
                        finRE.write(html)
                        finRE.close()
                        continue
                    str =  "https://github.com" + str
                    fin2.write(str)
                    continue
    fin2.close()
            
    with open("3.txt", "w+", encoding='UTF-8') as fin3:
        for line in open("2.txt", encoding='UTF-8'):
            #print(line)
            str = line[line.rfind('/') + 1 : line.find("\n")]
            #print(str)

            folder = os.getcwd() +  "\\" + list + "\\" + str

            if not os.path.exists(folder):
                os.makedirs(folder)

            line = line[line.find("github.com") + 10 : line.find("/tree")] + line[line.find("/tree") + 5 : line.find("\n")]
            strUlr = "https://raw.githubusercontent.com" + line + "/" + str + ".list"
            print(strUlr)
            str = folder + "\\" + str + ".list"

            html = requests.get(strUlr).text
            fin = open(str, "w+", encoding='UTF-8')
            fin.write(html)
            fin.close()





if __name__ == "__main__":
    #pullios7("https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Surge", "Surge")
    #pullios7("https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/QuantumultX", "QuantumultX")

    #os.remove("1.txt")
    #os.remove("2.txt")
    #os.remove("3.txt")
    print("hello ios")
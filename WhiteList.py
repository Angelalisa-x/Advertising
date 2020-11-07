
import requests, re
import shutil

from bs4 import BeautifulSoup

class WhiteList:

    def pull():
        url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/WhiteList/WhiteList.list'
        html = requests.get(url).text
        #print(html)

        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("WhiteList_1.txt","a+")
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
            if "@" in line:
                continue
            if "//" in line:
                continue
            if "$" in line:
                continue
            if "。" in line:
                continue
            if "USER-AGENT" in line:
                continue

            str=[]
            str = line
            str = str[str.find(',')+1: str.rfind(',')] + "\n"
            fwhite.write(str)

            #str = str[0:str.find(',')] + "\n"
            #str = "HOST," + str
            #str = str + ",Advertising" + "\n" 
        fwhite.close()

        return html

    def pull2():
        url = 'https://raw.githubusercontent.com/Potterli20/filtering/master/filtering.txt'
        html = requests.get(url).text
        #print(html)

        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("WhiteList_1.txt","a+")
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
            #str = str[str.find(',')+1: str.rfind(',')] + "\n"
            

            #str = str[0:str.find(',')] + "\n"
            #str = "HOST," + str
            #str = str + ",Advertising" + "\n" 
        fwhite.close()
        #return html
    
    #def pull3():
        url = 'https://raw.githubusercontent.com/liwenjie119/adg-rules/master/white.txt'
        html = requests.get(url).text
        #print(html)

        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("WhiteList_1.txt","a+")
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
            #str = str[str.find(',')+1: str.rfind(',')] + "\n"
            

            #str = str[0:str.find(',')] + "\n"
            #str = "HOST," + str
            #str = str + ",Advertising" + "\n" 
        fwhite.close()
        return html
    
    def pull4():
        url = 'https://raw.githubusercontent.com/Angelalisa-x/Advertising/master/WhiteList.txt'
        html = requests.get(url).text
        #print(html)
        return html

    # def pull5():
    #     url = 'https://raw.githubusercontent.com/pluwen/china-domain-allowlist/master/allow-list.sorl'
    #     html = requests.get(url).text
    #     #print(html)
    #     return html

    def pull6():
        url = 'https://raw.githubusercontent.com/HXHGTS/WhiteList/master/WhiteList.txt'
        html = requests.get(url).text
        #print(html)
        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("WhiteList_1.txt","a+")
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
            str = str[str.find('[/')+2: str.rfind('/]')] + "\n"
            fwhite.write(str)

            #str = str[0:str.find(',')] + "\n"
            #str = "HOST," + str
            #str = str + ",Advertising" + "\n" 
        fwhite.close()

    #def pull7():
        url = 'https://raw.githubusercontent.com/etotakeo/AdGuardDNSPassList/master/DNS-Pass-List'
        html = requests.get(url).text
        #print(html)

        with open("whiteList1.txt","w") as f:
            f.write(html)
        f.close()

        fwhite=open("WhiteList_1.txt","a+")
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
            #str = str[str.find(',')+1: str.rfind(',')] + "\n"
            

            #str = str[0:str.find(',')] + "\n"
            #str = "HOST," + str
            #str = str + ",Advertising" + "\n" 
        fwhite.close()
        return html
 

import requests, re
import shutil

from bs4 import BeautifulSoup

class WhiteList:

    def pull():
        url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/WhiteList/WhiteList.list'
        html = requests.get(url).text
        #print(html)
        return html

    def pull2():
        url = 'https://raw.githubusercontent.com/Potterli20/filtering/master/filtering.txt'
        html = requests.get(url).text
        #print(html)
        return html
    
    def pull3():
        url = 'https://raw.githubusercontent.com/liwenjie119/adg-rules/master/white.txt'
        html = requests.get(url).text
        #print(html)
        return html
    
    def pull4():
        url = 'https://raw.githubusercontent.com/Angelalisa-x/Advertising/master/WhiteList.txt'
        html = requests.get(url).text
        #print(html)
        return html
 
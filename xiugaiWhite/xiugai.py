
import sys,os
import shutil
from pathlib import Path

def copyFileOut():
    shutil.copy("../WhiteList/swhiteList.txt", os.path.join(os.path.dirname(__file__)))

    shutil.copy("../CustomRuleAD/CustomRuleAD.py", os.path.join(os.path.dirname(__file__)))
    shutil.copy("../Surge/SurgeCustomRuleAD.py", os.path.join(os.path.dirname(__file__)))

def copyFileIn():
    shutil.copy("CustomRuleAD_Ex.py", os.path.join(os.path.dirname(__file__),'../CustomRuleAD'))
    shutil.copy("SurgeCustomRuleAD_Ex.py", os.path.join(os.path.dirname(__file__),'../Surge'))

def DelFile():
    my_file = Path(os.path.join(os.path.dirname(__file__),'xiugaiWhite\__pycache__'))
    if my_file.exists():
        # 指定的文件或目录存在
        shutil.rmtree(os.path.join(os.path.dirname(__file__),'xiugaiWhite\__pycache__'))

    os.remove("swhiteList.txt")
    os.remove("CustomRuleAD.py")
    os.remove("SurgeCustomRuleAD.py")

    


def insertWhite(targetFile,readPath,whitePath):
    ctrl = 0
    fin = open(targetFile,"w",encoding='UTF-8')
    for line in open(readPath,"r",encoding='UTF-8'):
        str = []
        str = line
        str = str[0:str.find("\n")]
        if "######### yudong white #############" in line:
            ctrl = 1
        if ctrl == 1:
            for whiteLine in open(whitePath,"r",encoding='UTF-8'):
                strWhite = []
                strWhite = whiteLine
                strWhite = str[0:strWhite.find("\n")]
                if whiteLine == "\n":
                    continue
                whiteLine = whiteLine[0:whiteLine.find("\n")]

                strWhite = "        if \"" + whiteLine + "\" in line:" + "\n"
                fin.write(strWhite)
                fin.write("            continue" + "\n")
            ctrl = 0
        str = str + "\n"
        fin.write(str)
    fin.close()

if __name__ == '__main__':
    copyFileOut()
#Qx
    insertWhite("CustomRuleAD_Ex.py","CustomRuleAD.py","swhiteList.txt", )

#Surge
    insertWhite("SurgeCustomRuleAD_Ex.py","SurgeCustomRuleAD.py","swhiteList.txt", )

    copyFileIn()
    DelFile()


    # os.remove("whiteList1.txt")
    #shutil.rmtree("__pycache__")




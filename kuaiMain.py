# coding=utf-8
import sys,os
import shutil

sys.path.append( os.path.join(os.path.dirname(__file__),'CustomRuleAD'))
import CustomRuleAD

sys.path.append( os.path.join(os.path.dirname(__file__),'WhiteList'))
import whiteList

###################### CustomRuleAD ##################################
def doProcessCustomRuleAD():
    CustomRuleAD.doProcessCustomRuleAD()
    shutil.rmtree(os.path.join(os.path.dirname(__file__),'CustomRuleAD\__pycache__'))
    shutil.copy("KnightAD.list", os.path.join(os.path.dirname(__file__),'CustomRuleAD'))
    os.remove("KnightAD.list")

####################### WhiteList #########################################
def doProcessWhiteList():
    whiteList.doProcessWhiteList()
    shutil.rmtree(os.path.join(os.path.dirname(__file__),'WhiteList\__pycache__'))
    shutil.copy("whiteList.list", os.path.join(os.path.dirname(__file__),'WhiteList'))
    #os.remove("whiteList.list")

if __name__ == '__main__':
    doProcessCustomRuleAD()
    doProcessWhiteList()





    from pathlib import Path
    my_file = Path("__pycache__")
    if my_file.exists():
        # 指定的文件或目录存在
        shutil.rmtree("__pycache__")
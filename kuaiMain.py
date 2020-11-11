# coding=utf-8
import sys,os
import shutil
from pathlib import Path



###################### CustomRuleAD ##################################
def doProcessCustomRuleAD():
    sys.path.append( os.path.join(os.path.dirname(__file__),'CustomRuleAD'))
    import CustomRuleAD
    CustomRuleAD.doProcessCustomRuleAD()

    my_file = Path(os.path.join(os.path.dirname(__file__),'CustomRuleAD\__pycache__'))
    if my_file.exists():
        # 指定的文件或目录存在
        shutil.rmtree(os.path.join(os.path.dirname(__file__),'CustomRuleAD\__pycache__'))

    shutil.copy("KnightAD.list", os.path.join(os.path.dirname(__file__),'CustomRuleAD'))
    os.remove("KnightAD.list")

####################### WhiteList #########################################
def doProcessWhiteList():
    sys.path.append( os.path.join(os.path.dirname(__file__),'WhiteList'))
    import WhiteList
    WhiteList.doProcessWhiteList()

    my_file = Path(os.path.join(os.path.dirname(__file__),'WhiteList\__pycache__'))
    if my_file.exists():
        # 指定的文件或目录存在
        shutil.rmtree(os.path.join(os.path.dirname(__file__),'WhiteList\__pycache__'))

    shutil.copy("whiteList.list", os.path.join(os.path.dirname(__file__),'WhiteList'))
    os.remove("whiteList.list")

if __name__ == '__main__':
    doProcessCustomRuleAD()
    doProcessWhiteList()





    
    my_file = Path("__pycache__")
    if my_file.exists():
        # 指定的文件或目录存在
        shutil.rmtree("__pycache__")
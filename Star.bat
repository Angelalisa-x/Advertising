@echo off 

cd WhiteList
py %cd%\WhiteList.py

cd ..
cd xiugaiWhite
py %cd%\xiugai.py

cd ..
cd CustomRuleAD
py %cd%\CustomRuleAD_Ex.py

cd ..
cd Surge
py %cd%\SurgeCustomRuleAD_Ex.py

cd ..
cd Adguard
py %cd%\Adguard_Ex.py

cd ..

del %cd%\xiugaiWhite\CustomRuleAD_Ex.py \q \f \s 
del %cd%\xiugaiWhite\SurgeCustomRuleAD_Ex.py \q \f \s
del %cd%\xiugaiWhite\Adguard_Ex.py \q \f \s

del %cd%\CustomRuleAD\CustomRuleAD_Ex.py \q \f \s 
del %cd%\Surge\SurgeCustomRuleAD_Ex.py \q \f \s 
del %cd%\Adguard\Adguard_Ex.py \q \f \s

pause
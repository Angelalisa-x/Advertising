@echo off 

cd WhiteList
py %cd%\WhiteList.py

echo cd ..
echo cd xiugaiWhite
echo py %cd%\xiugai.py

echo cd ..
echo cd CustomRuleAD
echo py %cd%\CustomRuleAD_Ex.py

echo cd ..
echo cd Surge
echo py %cd%\SurgeCustomRuleAD_Ex.py

echo cd ..
echo cd Adguard
echo py %cd%\Adguard_Ex.py

cd ..
cd Rule
py %cd%\JS.py

cd ..

echo del %cd%\xiugaiWhite\CustomRuleAD_Ex.py \q \f \s 
echo del %cd%\xiugaiWhite\SurgeCustomRuleAD_Ex.py \q \f \s
echo del %cd%\xiugaiWhite\Adguard_Ex.py \q \f \s

echo del %cd%\CustomRuleAD\CustomRuleAD_Ex.py \q \f \s 
echo del %cd%\Surge\SurgeCustomRuleAD_Ex.py \q \f \s 
echo del %cd%\Adguard\Adguard_Ex.py \q \f \s

cd blackmatrix7
py %cd%\pullRuleSurge.py

cd ..

pause
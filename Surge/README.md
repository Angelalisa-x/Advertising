# CustomRuleAD

本项目的去广告测试版分流规则由爬虫程序自动维护。

定时爬取互联网上开源的去广告测试版分流规则，将其进行清洗、去重、合并、优化后，形成单一的分流规则文件，旨在解决引用大量外部规则造成规则重复的问题。

Surge 去广告规则：DOMAIN-SET,https://raw.githubusercontent.com/Angelalisa-x/Advertising/master/Surge/blackmatrix7.list,REJECT
        补充：RULE-SET,https://raw.githubusercontent.com/Angelalisa-x/Advertising/master/Surge/blackmatrix7_Ex.list,REJECT
        补充:DOMAIN-SET,https://raw.githubusercontent.com/Angelalisa-x/Advertising/master/Surge/KnightAD.list,REJECT

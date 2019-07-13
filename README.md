# tips-of-jx3 



01sync.py 是用来将 collections.xls 中的数据同步到数据库 collections.db 中    



02collections.py  

example:  
​        python 02collections.py 人物 渡会 ---- 得到该人物绝赞的菜  
​        python 02collections.py 品质 紫色 ---- 得到所有紫色物品的采集地点  
​        python 02collections.py 物品 佛珠 ---- 得到佛珠的采集地点  

collections.db 的数据库结构如下：   

CREATE TABLE sqlite_sequence(name,seq);  
CREATE TABLE collection_infos (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOCATION TEXT NOT NULL, ADDRESS TEXT NOT NULL, THING TEXT NOT NULL, QUALITY TEXT NOT NULL);  
CREATE TABLE foods (ID INTEGER PRIMARY KEY AUTOINCREMENT, FULL INTEGER NOT NULL, FAVOR INTER NOT NULL, POT TEXT NOT NULL, ADDON TEXT, GOOD TEXT, NAME TEXT NOT NULL, MATERIALS TEXT);  




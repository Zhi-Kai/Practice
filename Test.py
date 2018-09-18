# Import .json file
import json
import codecs
#=================================================#
# Reading data example

# my_list = []
# with open('naming base.json', 'r', encoding="utf8") as read_f:
#     for row in read_f.readlines():
#         # strip("\n") 去除換行符號
#         my_list.append(row.strip('\n'))
 
# for data in my_list:
#     print(data)



#=================================================#
# unsafety
# basefile = open('naming base.json','r',encoding='utf8')
# Database = json.loads(basefile.read())
# print(Database)



#=================================================#
#safety
#using read() to transfer *.json file to string
with open('naming base.json','r',encoding="utf8") as basefile:
    Database = json.loads(basefile.read())
    Date = json.dumps(basefile.read())    
# print(Database)
# print(basefile)

#=================================================#
#codecs application
#reading *.json file to string
with codecs.open('naming base.json','r','utf8') as basefile2:
    Database2 = json.load(basefile2)
# print(Database2)
# print (Database2.get("Signal1"))
# print(Database2["Signal1"])

# get value from *.json file
Datebace2_1 = Database["Signal1"]
print(Datebace2_1["Function_group"])
#=================================================#























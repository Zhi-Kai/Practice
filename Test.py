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
Database2_1 = Database["Signal1"]
print(Database2_1["Function_group"])

#set the port
Using_port = int(input())
Database2_2 = Database["Signal3"]
Database2_2["port"] = Using_port
print(Database2_2)
# for i in range(Database2_2(len)):
#     print(Databace2_2[i],end='')
#print(Database2_2["head"],Database2_2["port"],Database2_2["signal name"][1],Database2_2["R or C"])
#=================================================#
#a = Database2_2["head"],Database2_2["port"],Database2_2["signal name"][1],Database2_2["R or C"]
b = '%s%d%s%s' % (Database2_2["head"],Database2_2["port"],Database2_2["signal name"][1],Database2_2["R or C"])
print(b)






















# Import .json file
import json
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
with open('naming base.json','r',encoding="utf8") as basefile:
    Database = json.loads(basefile.read())    
print(Database)

#=================================================#





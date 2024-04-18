#!/usr/bin/env python3
import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    # for each in data:
    #     mylist = data[each]
    #     print(mylist)


# with open('chacon.csv', 'a') as file:
#     for each in data[:5]:
#         name = each['name']
#         html_url = each['html_url']
#         updated_at = each['updated_at']     
#         visibility = each['visibility']
#         line = name+","+html_url+"",updated_at+","+visibility
#         file.write(line)

opened = open('chacon.csv', 'a')
for each in data[:5]:
    line = each['name']+","+each['html_url']+","+each['updated_at']+","+each['visibility']+"\n"
    opened.write(line)

opened.close()
        



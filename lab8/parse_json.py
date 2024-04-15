#!/usr/bin/env python3
import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    for each in data:
        mylist = data[each]
        print(mylist)

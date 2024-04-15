#!/usr/bin/env python3
import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    for x in data:
        print('id')
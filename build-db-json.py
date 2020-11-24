import os
import json
import glob

os.chdir('./json-data')

data = [f for f in glob.glob('[0-9]*.json')]

cat_list = {}
style_list = []

with open('./categories.json') as c:
    cat = json.load(c)
    cat_list['categories'] = cat

for datum in data:
    print(datum)
    with open(datum) as f:
        style = json.load(f)
        style_list.append(style)

os.chdir('./')

with open('test-db.json', 'w') as db:
    cat_list['styles'] = style_list
    j = json.dump(cat_list, db, indent=4)

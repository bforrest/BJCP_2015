import os
import sys
import glob
import json
import re
from bs4 import BeautifulSoup

os.chdir('./dev.bjcp.org')
categories = []

cat_id = re.compile('\d+')
style_id = re.compile('\d+[A-Z]?')


def get_content(domset, classname):
    content = ''
    try:
        return domset.find('div', {'class': classname}).text

    except AttributeError:
        print('attribute error')
    except RuntimeError:
        print('classname %s not found' % classname)

    return content


def get_inner_text(domset, classname):
    content = []
    tag = domset.find('div', {'class': classname})
    if tag:
        p = tag.findAll('p')
        for item in p:
            if item.text:
                content.append(item.text)
    return content


def parse_vitals(domset):
    stats = []
    tag = domset.find('div', {'class': 'vital-statistics'})
    if(tag == None):
        return

    rows = tag.findAll('div', {'class': 'row'})

    for item in rows:
        stat = item.find('h3').text
        value = item.find('p').text
        stats.append({'stat': stat, 'value': value})
    return stats


def parse_attributes(domset):
    atts = []
    tag = domset.find('div', {'class': 'style-attributes'})
    if(tag == None):
        return
    anchors = tag.findAll('a')

    for item in anchors:
        atts.append({'tag': item.text, 'link': item['href']})
    return atts


def parse_style(domset):
    appearance = "".join(get_inner_text(domset, 'appearance'))
    aroma = "".join(get_inner_text(domset, 'aroma'))
    flavor = "".join(get_content(domset, 'flavor'))
    mouthfeel = "".join(get_content(domset, 'mouthfeel'))
    comments = "".join(get_inner_text(domset, 'comments'))
    comparison = get_content(domset, 'style-comparison')
    history = get_content(domset, 'history')
    ingredients = get_content(domset, 'ingredients')

    commercial = get_content(domset, 'commercial-examples')
    attributes = parse_attributes(domset)
    impression = get_content(domset, 'overall-impression')
    statistics = parse_vitals(domset)

    mystyle = {'impression': impression,
               'appearance': appearance,
               'aroma': aroma,
               'flavor': flavor,
               'mouthfeel': mouthfeel,
               'comments': comments,
               'comparison': comparison,
               'history': history,
               'ingredients': ingredients,
               'statistics': statistics,
               'commercial': commercial,
               'attributes': attributes
               }
    return mystyle


def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        broth = BeautifulSoup(content, 'lxml')
        articles = broth.findAll('article')

        categorytag = articles[0]
        header = categorytag.find('h1')
        category = header.text.strip('\t\n')
        description = get_content(categorytag, 'entry-content')
        instructions = get_content(categorytag, 'entry-instructions')

        categories.append({'id': cat_id.match(category).group(),
                           'category': category, 'description': description, 'instructions': instructions})

        top = len(articles)
        for substyle in range(1, top):
            style = articles[substyle].find('h1').text.strip('\t\n')

            mystyle = parse_style(articles[substyle])

            print('style %s' % style)
            mystyle['name'] = style

            cd = style_id.match(style)
            if cd:
                mystyle['id'] = cd.group(0)

            catid = cat_id.match(category)
            if catid:
                mystyle['categoryId'] = catid.group(0)

            mystyle['category'] = category
            mystyle['entry-content'] = description

            path = '/Users/barryforrest/Projects/MyGithub/BJCP_2015/json-data/%s.json' % style.strip()
            fj = open(path, 'w')
            j = json.dump(mystyle, fj,  sort_keys=False, indent=4)
            print(j)


def output_category_list():
    catpath = '/Users/barryforrest/Projects/MyGithub/BJCP_2015/json-data/categories.json'
    with open(catpath, 'w') as fc:
        j = json.dump(categories, fc, indent=4)
        print(j)


data = [f for f in glob.glob("*.html")]

for datum in data:
    print(datum)
    parse_file(datum)

output_category_list()

# pass dom-set and class name, get the inner-text

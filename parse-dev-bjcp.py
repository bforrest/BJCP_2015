import os
import sys
import glob
import json
import re
from bs4 import BeautifulSoup

os.chdir('./dev.bjcp.org')
categories = []


def get_content(domset, classname):
    content = ''
    try:
        content = domset.find(
            'div', {'class': classname}).text
    except AttributeError:
        print('attribute error')
    except RuntimeError:
        print('classname %s not found' % classname)

    return content


def parse_style(domset):
    appearance = get_content(domset, 'appearance')
    aroma = get_content(domset, 'aroma')
    flavor = get_content(domset, 'flavor')
    mouthfeel = get_content(domset, 'mouthfeel')
    comments = get_content(domset, 'comments')
    comparison = get_content(domset, 'style-comparison')
    history = get_content(domset, 'history')
    ingredients = get_content(domset, 'ingredients')
    statistics = get_content(domset, 'vital-statistics')
    commercial = get_content(domset, 'commercial-examples')
    attributes = get_content(domset, 'style-attributes')
    impression = get_content(domset, 'overall-impression')
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
        # first one is a category description

        categories.append({'category': category, 'description': description, })

        # top = len(articles)
        # for substyle in range(1, top):
        #     style = articles[substyle].find('h1').text.strip('\t\n')

        #     mystyle = parse_style(articles[substyle])

        #     print('style %s' % style)
        #     mystyle['name'] = style
        #     mystyle['category'] = category
        #     mystyle['entry-content'] = description

        #     path = '/Users/Barry/Projects/BeerStyles/BJCP_2015/json-data/%s.json' % style
        #     fj = open(path, 'w')
        #     j = json.dump(mystyle, fj,  sort_keys=False, indent=4)
        #     print(j)


data = [f for f in glob.glob("*.html")]

for datum in data:
    print(datum)
    parse_file(datum)

catpath = '/Users/barryforrest/Projects/MyGithub/BJCP_2015/json-data/categories.json'
with open(catpath, 'w') as fc:
    j = json.dump(categories, fc, indent=4)
    print(j)
# pass dom-set and class name, get the inner-text

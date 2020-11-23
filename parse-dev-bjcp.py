import os
import sys
import glob
import json
import re
from bs4 import BeautifulSoup

os.chdir('./dev.bjcp.org')


def get_content(domset, className):
    content = ''
    try:
        content = domset.find(
            'div', {'class': className}).text
    except AttributeError:
        print('attribute error')
    except RuntimeError:
        print('classname %s not found' % className)

    return content


def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        broth = BeautifulSoup(content, 'lxml')
        articles = broth.findAll('article')

        categoryTag = articles[0]
        header = categoryTag.find('h1')
        category = header.text.strip('\t\n')
        description = get_content(categoryTag, 'entry-content')
        # first one is a category description
        print(category)
        print(description)

        top = len(articles)
        for substyle in range(1, top):
            style = articles[substyle].find('h1').text.strip('\t\n')
            impression = get_content(articles[substyle], 'overall-impression')
            appearance = get_content(articles[substyle], 'appearance')
            aroma = get_content(articles[substyle], 'aroma')
            flavor = get_content(articles[substyle], 'flavor')
            mouthfeel = get_content(articles[substyle], 'mouthfeel')
            comments = get_content(articles[substyle], 'comments')
            comparison = get_content(articles[substyle], 'style-comparison')
            history = get_content([substyle], 'history')
            ingredients = get_content(articles[substyle], 'ingredients')
            statistics = get_content(articles[substyle], 'vital-statistics')
            commercial = get_content(articles[substyle], 'commercial-examples')
            attributes = get_content(articles[substyle], 'style-attributes')

            print('style %s' % style)
            myStyle = {'name': style,
                       'category': category,
                       'entry-content': description,
                       'impression': impression,
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
            path = '/Users/Barry/Projects/BeerStyles/BJCP_2015/json-data/%s.json' % style
            fj = open(path, 'w')
            j = json.dump(myStyle, fj,  sort_keys=False, indent=4)
            print(j)


data = [f for f in glob.glob("*.html")]

for datum in data:
    print(datum)
    parse_file(datum)
# pass dom-set and class name, get the inner-text

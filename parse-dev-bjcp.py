import os
import glob
from bs4 import BeautifulSoup

os.chdir('./dev.bjcp.org')

# data = [f for f in glob.glob("*.html")]

# for datum in data:
#     print(datum)

with open('category-21.html', 'r') as file:
    content = file.read()
    broth = BeautifulSoup(content, 'lxml')
    # tags within the page for style content.
    articles = broth.findAll('article')

    categoryTag = articles[0]
    header = categoryTag.find('h1')
    category = header.text
    description = categoryTag.find('p').text
    # first one is a category description
    print(category)
    print(description)

    top = len(articles)
    for substyle in range(1, top):
        style = articles[substyle].find('h1').text

        impression = get_content(articles[substyle], 'overall-impression)

        appearance = articles[substyle].find(
            'div', {'class': 'appearance'}).text
        aroma = articles[substyle].find('div', {'class': 'aroma'}).text
        flavor = articles[substyle].find('div', {'class': 'flavor'}).text
        mouthfeel = articles[substyle].find('div', {'class': 'mouthfeel'}).text
        comments = articles[substyle].find('div', {'class': 'comments'}).text
        comparison = articles[substyle].find(
            'div', {'class': 'style-comparison'}).text
        history = articles[substyle].find('div', {'class': 'history'}).text
        ingredients = articles[substyle].find(
            'div', {'class': 'ingredients'}).text
        statistics = articles[substyle].find(
            'div', {'class': 'vital-statistics'}).text
        commercial = articles[substyle].find(
            'div', {'class': 'commercial-examples'}).text
        attributes = articles[substyle].find(
            'div', {'class': 'style-attributes'}).text

        print('style %s' % style)
        myStyle = {'name': style, 'impression': impression}
        print(myStyle)
# articles = broth.findAll('article')


def get_content(ResultSet domset, className):
    try:
        return = domset.find(
            'div', {'class': 'overall-impression'}).text
    catch ValueError:
        print('classname %s not found' % className)
        return

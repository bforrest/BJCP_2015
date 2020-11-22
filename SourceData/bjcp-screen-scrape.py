import os
import requests
import re
import csv
from bs4 import BeautifulSoup

os.chdir('./dev.bjcp.org')
baseUrl = 'https://dev.bjcp.org/style/2015/%s'

# start range at 1 and go until 34
for category in range(1, 35):
    requestUri = baseUrl % category
    print(requestUri)
    r = requests.get(requestUri)
    outStyle = open('category-%s.html' % category, 'wb')
    outStyle.write(r.content)
    outStyle.close()
    # stash content for experiments
    #broth = BeautifulSoup(r.content, 'lxml')

    #articles = broth.findAll('article')

print('data retrieved')

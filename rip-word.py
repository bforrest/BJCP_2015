import os
from os import lseek
import zipfile
import re
import xml.dom.minidom
import codecs


os.chdir('./SourceData')

document = zipfile.ZipFile('./2015_Guidelines_Beer.docx')

uglyXml = xml.dom.minidom.parseString(document.read(
    'word/document.xml')).toprettyxml(indent='  ')

document.close()

text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
prettyXml = text_re.sub('>\g<1></', uglyXml)
kill_whitespace = prettyXml.replace(' xml:space="preserve"', '')

with open('pretty.xml', 'w') as f:
    # f.write(prettyXml)
    f.write(kill_whitespace.encode('utf8'))

# print(prettyXml)


text_list = re.findall(
    '(?<=<w:t>)(.*?)(?=<\/w:t>)', kill_whitespace)[1:]

f = open('just-the-text.txt', 'w')
f.write(codecs.BOM_UTF8)
for item in text_list:
    f.write(item.encode('utf-8') + '\n')
f.close()
g = open('just-the-text.txt')
print(g.read())
# print(text_list)

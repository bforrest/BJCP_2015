import os
from os import lseek
import zipfile
import re
import xml.dom.minidom


document = zipfile.ZipFile('./2015_Guidelines_Beer.docx')

uglyXml = xml.dom.minidom.parseString(document.read(
    'word/document.xml')).toprettyxml(indent='  ')

document.close()

text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
prettyXml = text_re.sub('>\g<1></', uglyXml)

with open('pretty.xml', 'w') as f:
    f.write(prettyXml.encode('utf8'))

print(prettyXml)

text_list = re.findall('(?:<w:t[^>]+>)(.*?)(?=<\/w:t>)', prettyXml)[1:]
print(text_list)

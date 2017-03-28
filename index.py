import sys, os
import urllib2
from bs4 import BeautifulSoup

def parser():
    request = urllib2.urlopen("https://github.com/sreetamdas")
    page_source = request.read()
    soup = BeautifulSoup(page_source,"html.parser")
    count = 0
    for element in soup.find_all(attrs={"data-date": "2017-03-27"}): #"fill": "#ebedf0"
        element = str(element)
        element = element.replace('=', ':')
        element = element.replace('" ', '", ')
        element = element.replace('<rect', '')
        element = element.replace('></rect>', '')
        mydict = dict((k.strip(), v.strip()) for k, v in
                      (item.split(':"') for item in element.split('", ')))
        print mydict
        print mydict['data-date']
        count += 1
    print count
"""
git commit --allow-empty --date="Sat Nov 14 14:00 2015 +0100" -m '2 Dec commit'
"""
# print "Input username : ",
# username = raw_input()

parser()

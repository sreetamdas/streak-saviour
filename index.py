import sys, os
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

def streaker(username):
    request = urllib2.urlopen("https://github.com/" + username)
    page_source = request.read()
    soup = BeautifulSoup(page_source,"html.parser")
    count = 0
    for element in soup.find_all(attrs={"fill": "#ebedf0"}):
        element = str(element)
        element = element.replace('=', ':')
        element = element.replace('" ', '", ')
        element = element.replace('<rect', '')
        element = element.replace('></rect>', '')
        mydict = dict((k.strip(), v.strip()) for k, v in
                      (item.split(':"') for item in element.split('", ')))
        t = datetime.strptime(mydict['data-date'] + '-07:00', '%Y-%m-%d-%H:%M')
        final_date = datetime.strftime(t, '%a %b %d %H:%M %Y')
        print final_date
        os.system('git commit --allow-empty --date="' + final_date + ' +0530" -m "' + final_date + ' commit"')
        count += 1
    print count

print "Input username : ",
github_username = raw_input()

streaker(github_username)

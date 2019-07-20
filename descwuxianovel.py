import urllib2
from bs4 import BeautifulSoup

def info(novelname):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://m.wuxiaworld.co/"+novelname+"/"
    headers={'User-Agent':user_agent,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, features="html.parser")
    for textp in soup.find_all("p", class_="review"):
        print textp.contents
        print textp
        print textp.getText()

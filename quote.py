# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests

#quotesitetobeadded=["https://www.goodreads.com/quotes/tag/mortality","https://www.brainyquote.com/topics/mortality","http://www.wiseoldsayings.com/mortality-quotes/"]

def clearStr(string):
    singleLine=string.replace('\n', ' ').replace('\r', '')
    return singleLine

def goodreads(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html.encode("ascii", "replace"),'html.parser')
    for quotedata in soup.find_all('div', attrs={'class': 'quoteText'}):
        quote= quotedata.find('br').previousSibling
        quote=quote.encode("utf-8").strip()
        print clearStr(quote)

goodreads("https://www.goodreads.com/quotes/tag/mortality")


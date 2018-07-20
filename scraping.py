'''scraping.py'''
import os
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from secret import ph , web , email

if os.path.exists("PDXSurplus.txt"):
    os.remove("PDXSurplus.txt")

for i in range(0,10):
    html = urlopen("%s"% str(web) + str(i))
    soup = BeautifulSoup(html, "html.parser")
    f = open("PDXSurplus.txt", "a+")
    f.write(soup.prettify())

f = open('PDXSurplus.txt')

searching = ('cisco','Cisco','CISCO')

for line in f.readlines():
    for word in searching:
        if word in line.split():
            os.system('mail -s "cisco item on PDX surplus website'\
                      ' https://www.pdx.edu/surplus/items-for-sale"'\
                      ' %s@vtext.com < /dev/null' % str(ph))
            os.system('echo "The scraper has found a cisco item on'\
                      ' the PDX surplus site https://www.pdx.edu/su'\
                      'rplus/items-for-sale" | mail -s "cisco found'\
                      ' on PDX Surplus" %s@gmail.com' % str(email))

f.close()

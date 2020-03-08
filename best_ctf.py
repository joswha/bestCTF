import requests 
import re
from lxml.html import fromstring

f = open('whoisthebest.txt', 'w')

for i in range(1000):
   r = requests.get("https://ctftime.org/event/" + str(i),headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0"})
   title = re.search(r"<title>(.+)<\/title>", r.content).group(1)
   nr  = r.text.count('place_ico')
   f.write(title + " number of participants " + str(nr) + '\n')

f.close()

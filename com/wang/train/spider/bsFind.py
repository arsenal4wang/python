import urllib2
from bs4 import BeautifulSoup

url = "http://www.nmc.cn/publish/forecast/AHA.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

city=soup.find_all(class_ = 'cname')

# print city
# print len(city)

for i in range(0,len(city)/2):
      other=city[i].find_next_siblings()
      print city[i].a.string.strip() +"\t\t" +other[0].string.strip()+"\t    "+other[1].string.strip()






__author__ = 'Administrator'

import urllib2
from bs4 import BeautifulSoup


def getRankMessage(url):
   page = urllib2.urlopen(url)
   contents = page.read()
   soup = BeautifulSoup(contents)
   allReaord=soup.findAll('tr')
   title=allReaord[0].th.find_next_siblings()
   print title
   print ("%s %6s %6s %6s %6s %6s %6s"%(allReaord[0].th.string,title[0].string,title[1].string,title[2].string,title[3].string,title[4].string,title[9].string))

   for i in range(1,len(allReaord)):
     tempRecord= allReaord[i].td.find_next_siblings()
     if 5< len(tempRecord):
       print ("%s %8s %6s %8s %8s %6s %8s "%(allReaord[i].td.string,tempRecord[0].a.string.strip(),tempRecord[1].string,tempRecord[2].string,tempRecord[3].string,tempRecord[4].string,tempRecord[9].string))

getRankMessage('http://goal.sports.163.com/39/stat/standings/2015_3.html');
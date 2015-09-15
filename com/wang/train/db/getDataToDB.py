#coding=utf8
import urllib2
import MySQLdb
from bs4 import BeautifulSoup
import datetime


def getRankMessage(url):
   page = urllib2.urlopen(url)
   contents = page.read()
   soup = BeautifulSoup(contents)
   allReaord=soup.findAll('tr')
   return allReaord


def insertIntoDB(allReaord,type):

   db = MySQLdb.connect("localhost", "root", "wang", "wang", charset="utf8")
   cursor = db.cursor()

   for i in range(1,len(allReaord)):
       tempRecord= allReaord[i].td.find_next_siblings()
       if 5 < len(tempRecord):
           _type = type.decode("utf8")
           _team = tempRecord[0].a.string.strip()
           _rank = allReaord[i].td.string
           _round = tempRecord[1].string
           _win_num = tempRecord[2].string
           _ping_num = tempRecord[3].string
           _lose_num = tempRecord[4].string
           _cur_score = tempRecord[9].string
           now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").strip()
           print(now)
           sql='insert INTO  football(type,team,rank,round,win_num,ping_num,lose_num,cur_score,c_time) VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % \
                                     (_type,_team,_rank,_round,_win_num,_ping_num,_lose_num,_cur_score,now)
           cursor.execute(sql)
           db.commit();
   db.close()

def insetDB():
    five ={'39':'英超','51':'意甲','49':'德甲','54':'西甲','68':'法甲'}
    keys=['39','51','49','54','68']
    for i in range(0,len(keys)):
         key = keys[i]
         url = 'http://goal.sports.163.com/'+key+'/stat/standings/2015_3.html'
         insertIntoDB(getRankMessage(url),five[key])

insetDB()
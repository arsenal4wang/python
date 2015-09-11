# coding=utf-8
import MySQLdb


db = MySQLdb.connect("localhost", "root", "wang", "wang", charset="utf8")
cursor = db.cursor()
# count=cursor.execute("select * from user ")
sql = """INSERT INTO user(name,pass)
         VALUES ('wang', 'password')"""

# result=cursor.fetchall()
# print result

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

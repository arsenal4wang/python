import MySQLdb

def getDBConn():
    db=MySQLdb.connect('localhost','root','wang','wang',charset='utf8')
    return  db

def getCusor():
    return  getDBConn().cursor()

def show_insert(vars,*args):
    db = getDBConn()
    cursor =db.cursor()
    sql = 'insert into user VALUES ("%s","%s")' % \
          (vars,args[0])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def show_delete(vars,*args):
    db = getDBConn()
    cursor =db.cursor()
    sql = 'delete from user where pass= "%s"' % (vars)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def show_update(vars,*args):
    db = getDBConn()
    cursor =db.cursor()
    sql = 'update  user set name = "%s" where pass = "%s"' % (vars, args[0])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def show_select(name):
    cursor= getCusor()
    sql = "select * from user WHERE name= '%s' " % (name)
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print i[0] + "  "+ i[1]






show_select("wang")
print 'insert a user'
show_insert('likeqiang','wanggg')

print  'delete a user'
show_delete('wanggg')

print  'update a user'
show_update('wangygg','pass')
# show_select('wang')





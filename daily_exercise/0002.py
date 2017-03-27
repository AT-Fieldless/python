#讲0001.txt中的内容插入mysql中
import MySQLdb

cxn = MySQLdb.connect(user = 'root',passwd = '741316636jzy')
cxn.query('USE python')
cur = cxn.cursor()
#cxn.query('CREATE TABLE users(jhm VARCHAR(30))')
file = open('0001.txt','r')

for i in range(200):
    f = file.readline()
    cur.execute('INSERT INTO users VALUES(%s)',(f,))
    cxn.commit()

cur.close()
cxn.commit()
cxn.close()

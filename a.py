
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
   conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='wmtest2',port=3306,charset='utf8')
   cur=conn.cursor()
   cur.execute('select * from students')
   
   data = cur.fetchall()
   for x in data:
      print x
      
   cur.close()
   conn.close()
except MySQLdb.Error,e:
   print "Mysql Error %d: %s" %(e.args[0],e.args[1])



#coding:utf-8
'''cursor 游标操作数据库表每一行;进行数据库操作 连接 得到连接 建立游标 得到游标 操作表'''
import MySQLdb,os
import json

#连接数据库函数
def conn_db():
    try:
        dbconn=MySQLdb.connect(host='42.62.67.249',port=4040,db='bw_gss_v2',user='root',passwd='mysql_Q!2wE#4rT%6y',charset='utf8')
    except Exception,e:
        return e
    else:
        return dbconn
    

   

def select_data(sql):
    conn=conn_db()
    if conn:
        cur=conn.cursor()#建立游标
        cur.execute(sql)#游标执行sql
        result=cur.fetchall()#执行结果赋给变量        

    cur.close()#关闭游标
    conn.close()#关闭数据库连接
    return result

sql="SELECT a.answer FROM `Answer_Original` a INNER JOIN `bw_gss_v2`.`Answer_Logs` b ON a.`AnswerLogID` = b.`AnswerLogID` WHERE b.`IssueID` = '2274'"


#接收并处理处理库返回值
re=select_data(sql)
re_list=list(re)


cnt_i=len(re_list)


i=j=0
while i<cnt_i:    
    cnt_j=len(re_list[i])   
    while j<cnt_j:
        print i
        print j
        print re_list[i][j]
        list1=[]
        print type(list1)
        list1=re_list[i][j]
        print list1
        print type(list1)
 
        j+=1
    i+=1
    if i==0:
        break
else:
    print 'end'

    





    

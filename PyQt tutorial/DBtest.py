import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='world',
        )
#创建游标以访问数据库
cur = conn.cursor()


##在execute中传入要执行的sql语句 通过游标 执行操作数据库
##获得表中有多少条数据
datarec = cur.execute("select * from city where CountryCode = 'NLD'")

##打印查到的数据
info = cur.fetchmany(datarec)
for ii in info:
    print (ii)

##关闭游标
cur.close()

##向数据库插入时必须commit 否则不会将修改应用到数据库
conn.commit()

##关闭数据库
conn.close()
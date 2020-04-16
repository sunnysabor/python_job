import pymysql

# connect
conn = pymysql.connect(host="localhost", user="root",
                       password="123", database="wuye", charset="utf8")
cursor = conn.cursor()
sql = "select * from charge"
res = cursor.execute(sql)
ret=cursor.fetchall()
for r in ret:
    print(r)

# 定义要执行的sql语句
# sql = 'insert into userinfo(user,pwd) values(%s,%s);'
# data = [
#     ('july', '147'),
#     ('june', '258'),
#     ('marin', '369')
# ]
# 拼接并执行sql语句
# cursor.executemany(sql, data)

# 涉及写操作要注意提交
conn.commit()
cursor.close()
conn.close()

import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
cursor = connection.cursor()

sql = "insert into employee values (5,'Riya','IT',50000)"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfully")

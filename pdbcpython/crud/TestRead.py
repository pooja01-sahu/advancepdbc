import pymysql

connection = pymysql.connect(host='localhost', port=3306, password='root', user='root', db='user')
cursor = connection.cursor()
sql = "select * from employee";
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0], data[1], data[2], data[3])
connection.commit()
connection.close()
print("Data read successfully")

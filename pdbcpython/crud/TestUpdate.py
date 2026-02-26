import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
cursor = connection.cursor()
sql = "Update employee set name = 'Manjhari' where id = 4";
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Update Successfully")

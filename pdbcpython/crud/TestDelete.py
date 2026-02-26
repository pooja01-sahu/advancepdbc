import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
cursor = connection.cursor()
sql = "DELETE FROM employee WHERE ID =5"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Delete Successfully")

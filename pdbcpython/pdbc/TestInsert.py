import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',password='root',db='user')
cursor = connection.cursor()

# sql ="insert into employee values (3,'Tanvisha','IT',50000)"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("Data Inserted Successfully")

id = int(input("Enter Employee ID: "))
name = input("Enter Name: ")
department = input("Enter your Department: ")
salary = float(input("Enter your Salary: "))

insert_sql = "Insert into employee values(%s,%s,%s,%s)"
cursor.execute(insert_sql,(id,name,department,salary))
connection.commit()

print("Data inserted successfully\n")


import pymysql

def testinsert():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES (6, 'Mahi', 'Kasera', 70000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

def testinsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES (%s, %s, %s, %s)"
    data=(7,'Bubby','malviya',80000)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data Inserted2 Successfully")

def testInsert3(id, Name, LastName, Salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "insert into User values(%s, %s, %s, %s)"
    data = (id, Name, LastName, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted3 successfully')

def testInsert4(data={}):
    id = data['id']
    name = data['Name']
    LastName = data['LastName']
    Salary = data['Salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "insert into user values(%s, %s, %s, %s)"
    data = (id, name, LastName, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')




#testinsert()
#testinsert2()
#testInsert3(8,'Ravi','Kumar',90000)
testInsert4({'id':9,
             'Name':'Aman',
             'LastName':'Singh',
             'Salary':100000})
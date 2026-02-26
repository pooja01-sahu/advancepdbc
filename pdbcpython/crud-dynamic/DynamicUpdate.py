import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "update user set name = 'Rehmana' where id =2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "update user set name = %s where id = %s"
    data = ('Ravi', 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated2 successfully')


def testUpdate3(name, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "update user set name = %s where id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated3 successfully')


def testInsert4(data):
    id = data['id']
    name = data['Name']
    LastName = data['LastName']
    Salary = data['Salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "update user set name= %s, LastName= %s ,Salary %s where id = %s"
    data = (name, LastName, Salary, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')


# testUpdate1()
# testUpdate2()
# testUpdate3('Aman', 3)


params = {}
params['id'] = 2
params['Name'] = 'abc'
params['LastName'] = 'klj'
params['Salary'] = 100

testInsert4(params)
import pymysql


def testread1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()

    print("data Read Successfully")


def testread2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    columnName = ('id', 'name', 'LastName', 'Salary')
    for x in data:
        print(x)
        # print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()

    sql = "select * from user"
    # sql = "select * from user where id = 1"
    # sql = "select * from user where LastName = 'Kumar'"
    # sql = "select * from user where name like 'a%'"
    # sql = "select * from user where Salary = 50000"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
    connection.commit()
    connection.close()


def testRead4(id, name, lastname, salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()

    sql = 'select * from user'
    if id != 0:
        sql += " where id = " + str(id)
    if name != '':
        sql += " where name like '" + name + "%'"
    if lastname != '':
        sql += " where lastname like '" + lastname + "%'"
    if salary != 0:
        sql += " where salary = " + str(salary)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])

    connection.commit()
    connection.close()


def testRead5(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    lastname = param.get('lastname', '')
    salary = param.get('salary', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "select * from user where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if lastname != '':
        sql += " and lastname like '" + lastname + "%'"
    if salary != 0:
        sql += " and salary = " + str(salary)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
    connection.commit()
    connection.close()


def testRead6(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    lastname = param.get('lastname', '')
    salary = param.get('salary', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(
        host='localhost', port=3306, user='root', password='root', db='advancepython'
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM user WHERE 1=1"
    if id != 0:
        sql += " AND id = " + str(id)
    if name != '':
        sql += " AND name LIKE '" + name + "%'"
    if lastname != '':
        sql += " AND lastname LIKE '" + lastname + "%'"
    if salary != 0:
        sql += " AND salary = " + str(salary)

    # Pagination
    if pageSize > 0:
        offset = (pageNo - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print('sql =>', sql)

    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])

    connection.commit()
    connection.close()


# testread1()
# testread2()
# testRead3()
# testRead4(0, 'a', '', 0)

# testRead5({'name': ''})

param = {'id': 0,
         'name': 'Aman',
         'lastname': '',
         'salary': 0,
         'pageNo': 1,
         'pageSize': 2
         }

# testRead5(param)
testRead6(param)

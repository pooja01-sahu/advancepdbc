import pymysql


def createTable():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
    cursor = connection.cursor()
    sql = 'create table volunteer(volu_id  int primary key,volu_name varchar(50),phone varchar(50), availability varchar(50))'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("table is created")


createTable()

import pymysql


def createTable():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='categorymodule')
    cursor = connection.cursor()
    sql = "create table cate (category_id int primary key,category_name VARCHAR(50),Description VARCHAR(50),Active Boolean)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created Successfully")


createTable()

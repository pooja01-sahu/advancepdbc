import pymysql

def categoryDelete(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id= %s"
    data=(id,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete3 Successfully")
# testDelete()
#testdelete2()
categoryDelete(3)
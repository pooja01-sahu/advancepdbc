import pymysql


def volunteerInsert(volu_id,volu_name,phone,availability):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='user')
    cursor = connection.cursor()
    sql = 'insert into volunteer values(%s, %s ,%s, %s)'
    data = (volu_id,volu_name,phone,availability)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data is insert successfully")

volunteerInsert(4,"Tanvisha",9926886585,"Full-time")
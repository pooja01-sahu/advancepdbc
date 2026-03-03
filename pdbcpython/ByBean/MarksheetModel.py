import pymysql
from MarksheetBean import *



class MarksheetModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, mark: MarksheetBean):
      id = MarksheetModel.nextPk(self)
      rollno = mark.rollno
      name = mark.name
      physics = mark.physics
      chemistry = mark.chemistry
      maths = mark.maths
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advance_python')
      cursor = connection.cursor()
      sql = 'insert into marksheet values (%s,%s,%s,%s,%s,%s)'
      data = (id,rollno,name,physics,chemistry,maths)
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print('data inserted successfully')

    def get(self,id):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advance_python')
        cursor = connection.cursor()
        sql = 'select * from marksheet where id = %s'
        data = (id)
        cursor.execute(sql,data)
        result = cursor.fetchall()
        columnName =("id","rollno","name","physics","chemistry","maths")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def update(self, mark: MarksheetBean):
      id = mark.id
      rollno = mark.rollno
      name = mark.name
      physics = mark.physics
      chemistry = mark.chemistry
      maths = mark.maths
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='advance_python')
      cursor = connection.cursor()
      sql = 'update marksheet set rollno = %s,name = %s,physics = %s,chemistry = %s,maths = %s where id = %s'
      data = (rollno,name,physics,chemistry,maths,id)
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print('data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')







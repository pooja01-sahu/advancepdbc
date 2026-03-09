import pymysql
from DecorationBean import DecorationBean


class DecorationModule():

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host="localhost",port=3306,user="root",password="root",db = "user")
        cursor = connection.cursor()
        sql = "select max(DecorationId) from Decoration"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add (self,dec: DecorationBean):
     decorationId = DecorationModule.nextPk(self)
     theme = dec.Theme
     vendorName = dec.VendorName
     cost = dec.Cost
     connection = pymysql.connect(host="localhost",port=3306,password="root",user="root",db="user")
     cursor = connection.cursor()
     sql = "insert into decoration values (%s,%s,%s,%s)"
     data = (decorationId,theme,vendorName,cost)
     cursor.execute(sql,data)
     connection.commit()
     connection.close()
     print("data inserted successfully")

    def get(self,DecorationId):
        connection = pymysql.connect(host="localhost", port=3306, user="root", password="root",db="user")
        cursor = connection.cursor()
        sql = "select * from decoration where DecorationId = %s"
        data = (DecorationId)
        cursor.execute(sql,data)
        result = cursor.fetchall()
        columnName = ["decorationId","theme","vendorName","cost"]
        res = []
        for x in result:
            res.append({columnName[i] : x[i] for i ,_ in enumerate(x)})
        connection.close()
        return res

    def update(self, dec: DecorationBean):
        decorationId = dec.DecorationId
        theme = dec.Theme
        vendorName = dec.VendorName
        cost = dec.Cost
        connection = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="user")
        cursor = connection.cursor()
        sql = "update decoration set theme = %s,vendorName = %s,cost = %s where DecorationId = %s"
        data = (theme,vendorName,cost,decorationId)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("data updated successfully")

    def delete(self, decorationId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "delete from decoration where decorationId = %s"
        data = (decorationId)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')







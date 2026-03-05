import pymysql
from VenueBean import *

class VenueModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select max(venueId) from venue "
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, ven: VenueBean ):
      venueId = VenueModel.nextPk(self)
      venueName = ven.venueName
      city = ven.city
      capital = ven.capital
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='user')
      cursor = connection.cursor()
      sql = 'insert into venue values (%s,%s,%s,%s)'
      data = (venueId,venueName,city,capital)
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print('data inserted successfully')

    def get(self, venueId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = 'select * from venue where venueId = %s'
        data = (venueId)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("venueId", "venueName", "city", "capital")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def update(self, ven: VenueBean):
        venueId = ven.venueId
        venueName = ven.venueName
        city = ven.city
        capital = ven.capital
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = 'update venue set venueName = %s,city = %s,capital = %s where venueId = %s'
        data = (venueName, city, capital,venueId)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, venueId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "delete from venue where venueId = %s"
        data = (venueId)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')



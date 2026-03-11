import pymysql
from DonationCampBean import DonationCampBean

class DonationCampModule():

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="user")
        cursor = connection.cursor()
        sql = "select max(campId) from camp"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self,camp: DonationCampBean):
        campId  = DonationCampModule.nextPk(self)
        campName = camp.campName
        campDate = camp.campDate
        organizer = camp.organizer
        connection = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="user")
        cursor = connection.cursor()
        sql = "insert into camp values (%s,%s,%s,%s)"
        data = (campId,campName,campDate,organizer)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("data inserted successfully")


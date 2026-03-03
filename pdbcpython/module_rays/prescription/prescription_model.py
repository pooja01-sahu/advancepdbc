import pymysql
from module_rays.prescription.prescrption_bean import PrescriptionBean


class PrescriptionModel:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "select max(prescriptionId) from prescrption"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, pre: PrescriptionBean):
      prescriptionId = PrescriptionModel.nextPk(self)
      patientName = pre.patientName
      doctorName = pre.doctorName
      prescribedDate = pre.prescribedDate
      connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='user')
      cursor = connection.cursor()
      sql = 'insert into prescrption values (%s,%s,%s,%s)'
      data = (prescriptionId,patientName,doctorName,prescribedDate)
      cursor.execute(sql,data)
      connection.commit()
      connection.close()
      print('data inserted successfully')

    def get(self, prescriptionId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = 'select * from prescrption where prescriptionId = %s'
        data = (prescriptionId)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("prescriptionId", "patientName", "doctorName", "prescribedDate")
        res = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def update(self, pre: PrescriptionBean):
        prescriptionId = pre.prescriptionId
        patientName = pre.patientName
        doctorName = pre.doctorName
        prescribedDate = pre.prescribedDate
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = 'update prescrption set patientName = %s,doctorName = %s,prescribedDate = %s where prescriptionId = %s'
        data = (patientName, doctorName, prescribedDate,prescriptionId)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, prescriptionId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
        cursor = connection.cursor()
        sql = "delete from prescrption where prescriptionId = %s"
        data = (prescriptionId)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')



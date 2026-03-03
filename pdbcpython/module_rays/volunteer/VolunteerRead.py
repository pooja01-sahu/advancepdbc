import pymysql


def ReadVolunteer(param={}):
    volu_id = param.get('volu_id', 0)
    volu_name = param.get('volu_name', '')
    phone = param.get('phone', '')
    availability = param.get('availability', '')
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='user')
    cursor = connection.cursor()
    sql = "select * from volunteer where 1 = 1"
    if volu_id != 0:
        sql += "AND volu_id = " + str(volu_id)
    if volu_name != '':
        sql += "AND Volu_name LIKE '" + volu_name + "%"
    if phone != '':
        sql += "And phone LIKE " + phone + "%"
    if availability != '':
        sql += " AND availability = " + str(availability)

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


param = {'Volu_id': '1',
'volu_name': "",
'phone': "",
'availability' : '',
'pageNo': 1,
'pageSize': 2
}

ReadVolunteer(param)

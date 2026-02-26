import pymysql


# connection = pymysql.connect(host='localhost', port=3306, password='root', user='root', db='categorymodule')
# cursor = connection.cursor()
# sql = "select * from category";
# cursor.execute(sql)
# result = cursor.fetchall()
# for data in result:
#     print(data[0], data[1], data[2], data[3])
# connection.commit()
# connection.close()
# print("Data read successfully")


def categoryRead2(param={}):
    category_id = param.get('category_id', 0)
    category_name = param.get('category_name', '')
    Description = param.get('Description', '')
    Active = param.get('Active', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(
        host='localhost', port=3306, user='root', password='root', db='categorymodule'
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM category WHERE 1=1"
    if category_id != 0:
        sql += " AND category_id = " + str(category_id)
    if category_name != '':
        sql += " AND category_name LIKE '" + category_name + "%'"
    if Description != '':
        sql += " AND Description LIKE '" + Description + "%'"
    if Active != '':
        sql += " AND Active = " + str(Active)

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


param = {'category_id': '1',
         'category_name': 'Furniture',
         'Description': '',
         'Active': '',
         'pageNo': 1,
         'pageSize': 2
         }

categoryRead2(param)

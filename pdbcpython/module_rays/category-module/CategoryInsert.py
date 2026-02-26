import pymysql


def insertCategory(data={}):
    category_id = data['category_id']
    category_name = data['category_name']
    Description = data['Description']
    Active = data['Active']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='categorymodule')
    cursor = connection.cursor()
    sql = "insert into category values(%s, %s, %s, %s)"
    data = (category_id, category_name, Description, Active)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


insertCategory({'category_id': 3,
                'category_name': 'Clothing',
                'Description': 'Fashion Items',
                'Active': True})

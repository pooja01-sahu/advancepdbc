import pymysql


def categoryUpdate(data):
    category_id = data['category_id']
    category_name = data['category_name']
    Description = data['Description']
    Active = data['Active']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='categorymodule')
    cursor = connection.cursor()
    sql = "update category set category_name= %s, Description= %s ,Active = %s where category_id = %s"
    data = (category_name, Description, Active, category_id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data update successfully')


params = {}
params['category_id'] = 2
params['category_name'] = 'Furniture'
params['Description'] = 'Home Furniture'
params['Active'] = False

categoryUpdate(params)

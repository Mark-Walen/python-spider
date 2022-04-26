import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    # one = cursor.fetchone()
    # print('One:', one)
    # results = cursor.fetchall()
    # print('Results:', results)
    # print('Results type:', type(results))
    # for row in results:
    #     print(row)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')

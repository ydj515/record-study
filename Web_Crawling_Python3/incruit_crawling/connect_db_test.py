#-*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', db='test', charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = "select * from hoho;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()
import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='cfe9el6v1',
        database='dogodb'
    )
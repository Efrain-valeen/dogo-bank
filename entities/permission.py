from enums.value_permission import ValuePermission
from persistence.db import get_connection
import pymysql

class Permission:
    def __init__(self, id: int,  value: ValuePermission):
        self.id = id
        self.value = value

def get_by_user(id_user: int):
    try:
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        sql ="SELECT id, value from permission WHERE id_user = %s"
        cursor.execute(sql, (id_user,))
        rs = cursor.fetchall()

        permissions = []
        for r in rs:
            permissions.append(
                Permission(
                    r['id'], 
                    ValuePermission(r['value'])))
        return permissions
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        cursor.close()
        connection.close()

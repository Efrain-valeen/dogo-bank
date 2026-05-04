import pymysql
from enums.profile import Profile
from entities.permission import Permission
from persistence.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id: int, name:str, email:str, 
                 password:str, profile: Profile, 
                 permissions: list, is_active: bool):
        
        self.id= id
        self.name = name
        self.email = email
        self.password = password
        self.profile = profile
        self.permissions = permissions
        self.is_active = is_active


    def check_email_exists(email) -> bool:
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        sql = "SELECT email FROM user WHERE email = %s"
        cursor.execute(sql, (email,))
        row = cursor.fetchone()

        cursor.close()
        connection.close()

        return row is not None
    

    def save(name: str, email:str, password:str) -> bool:
        try:
            connection = get_connection()
            cursor = connection.cursor()

            hash_password = generate_password_hash(password)

            sql = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, hash_password))
            connection.commit()

            cursor.close()
            connection.close()

            return True
        except Exception as ex:
            print(f"Error saving user:{ex}")
            return False
        

    def check_login(email, password):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            sql = "SELECT id, name, email, password, profile, is_active FROM user WHERE email = %s"
            cursor.execute(sql, (email,))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user and check_password_hash(user["password"], password):

                # 🔥 FIX DEL PROFILE (aquí estaba el pedo)
                try:
                    profile = Profile(user["profile"])
                except:
                    profile = Profile(1)  # valor por defecto

                permissions = Permission.get_by_user(user["id"])

                return User(
                    user["id"],
                    user["name"],
                    user["email"],
                    user["password"],
                    profile,
                    permissions,
                    user["is_active"]
                )

            return None

        except Exception as ex:
            print(f"Error login user:{ex}")
            return None


    def get_by_id(id):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            sql = "SELECT id, name, email, password, profile, is_active FROM user WHERE id = %s"
            cursor.execute(sql, (id,))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                permissions = Permission.get_by_user(user["id"])

                # FIX DEL PROFILE
                try:
                    profile = Profile(user["profile"])
                except:
                    profile = Profile(1)

                return User(
                    user["id"],
                    user["name"],
                    user["email"],
                    user["password"],
                    profile,
                    permissions,
                    user["is_active"]
                )

            return None

        except Exception as ex:
            print(f"Error get user:{ex}")
            return None
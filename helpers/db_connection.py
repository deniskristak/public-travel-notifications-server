import mysql.connector
from helpers.singleton import Singleton


class DbConnector(metaclass=Singleton):

    def __init__(self):
        self.__db = mysql.connector.connect(
            host="localhost",
            user="fastapi",
            password="password",
            database="public_travel"
        )
        self.__cursor = self.__db.cursor()

    def get_cursor(self):
        return self.__cursor

    def get_db(self):
        return self.__db


db_connection = DbConnector()

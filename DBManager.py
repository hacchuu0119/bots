# coding: UTF-8

import mysql.connector


class DBManager:
    def __init__(self, config):
        self.conn = mysql.connector.connect(  # このconnはself.mysql_connectionに格納してても、
            host=config['host'],  # どっかで使われて消えてるっぽい。
            port=config['port'],  # なのでクラス変数に
            user=config['user'],
            password=config['password'],
            database=config['database'],
        )

    def connector(self):
        return self.conn

    def commit(self):
        self.conn.commit()

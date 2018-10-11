# coding: UTF-8

import mysql.connector
from ConfigManager import Config


class DBManager:
    conn = None

    def __init__(self):
        pass

    @classmethod
    def set_db(cls):
        config = Config.get_config('DB')
        DBManager.conn = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
        )

    @classmethod
    def connector(cls):
        return DBManager.conn

    @classmethod
    def commit(cls):
        DBManager.conn.commit()

# coding: UTF-8

import configparser


class Config:
    config = configparser.ConfigParser()

    def parse(self, path):
        return []

    # これを直接呼ばない
    def __init__(self, path):
        self.parse(path)

    # コンフィグファイルのパスor名前を引数にとる
    @classmethod
    def set_config(cls, path):
        Config.config.read(path)

    # conf.iniの[DB]などを指定
    # 辞書型で返す
    @classmethod
    def get_config(cls, name):
        return Config.config[name]

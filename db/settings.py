from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from ConfigManager import Config
from pathlib import Path

config_path = Path.cwd() / "config.ini"

Config.set_config(config_path)
config = Config.get_config('DB')

# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    config['user'],
    config['password'],
    config['host'],
    config['database'],
)
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    # echo=True  # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()

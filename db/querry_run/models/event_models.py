import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from db.DBSettings import Base
from db.DBSettings import ENGINE
from ConfigManager import Config
from db.DBSettings import session


class WelcomeModel(Base):
    """
    ユーザモデル
    """

    __tablename__ = 'welcome_message'

    id = Column('id', primary_key=True)
    server = Column('server_name')
    channel = Column('channel_name')
    message = Column('message')


def main(args):
    """
    メイン関数
    """
    # Config.set_config('/Users/usr0200618/study/bot/config.ini')
    uu = session.query(WelcomeModel).all()
    print(type(uu))
    for u in uu:
        print(u.channel)


if __name__ == "__main__":
    main(sys.argv)

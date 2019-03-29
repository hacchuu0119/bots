from sqlalchemy import Column, Integer, String
from db.DBSettings import Base


class ServersModel(Base):
    """
    キーワード検索
    key_wordのDBモデル
    """

    __tablename__ = 'server_list'

    id = Column('id')
    name = Column('name', primary_key=True)


class UserModel(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))

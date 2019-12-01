from db.settings import Base, session
from sqlalchemy import *


class MatchAndResponseTable(Base):
    """
    キーワード検索
    match_replyのDBモデル
    """

    __tablename__ = 'match_and_response'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    match_word = Column('match_word', String, nullable=False)
    response_word = Column('response_word', TEXT, nullable=False)
    server_id = Column('server_id', Integer, nullable=False)
    author_id = Column('author_id', Integer, nullable=False)


def get_bot_response(user_response, guild_id):
    try:
        res = session \
            .query(MatchAndResponseTable.response_word) \
            .filter(MatchAndResponseTable.match_word == user_response, MatchAndResponseTable.server_id == guild_id) \
            .all()
    except:
        session.rollback()
        session.close()
        raise

    return res


def insert_bot_response(match_word, guild_id, response_value, user_id):
    try:
        mart = MatchAndResponseTable()
        mart.server_id = guild_id
        mart.match_word = match_word
        mart.author_id = user_id
        mart.response_word = response_value
        session.add(mart)
        session.commit()
    except:
        session.rollback()
        session.close()
        raise
    session.close()


def check_existence_bot_response(match_word, response_value, guild_id):
    try:
        res = session \
            .query(MatchAndResponseTable.response_word) \
            .filter(MatchAndResponseTable.match_word == match_word,
                    MatchAndResponseTable.server_id == guild_id,
                    MatchAndResponseTable.response_word == response_value) \
            .all()
    except:
        session.rollback()
        session.close()
        raise
    session.close()

    return res


def delete_all_key_bot_response(match_word, guild_id):
    try:
        session.query(MatchAndResponseTable) \
            .filter(MatchAndResponseTable.match_word == match_word,
                    MatchAndResponseTable.server_id == guild_id) \
            .delete()
    except:
        session.rollback()
        session.close()
        raise

    session.close()


def delete_one_bot_response(match_word, response_value, guild_id):
    try:
        session.query(MatchAndResponseTable) \
            .filter(MatchAndResponseTable.match_word == match_word,
                    MatchAndResponseTable.server_id == guild_id,
                    MatchAndResponseTable.response_word == response_value) \
            .delete()
    except:
        session.rollback()
        session.close()
        raise

    session.close()

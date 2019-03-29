from db.DBSettings import Base
import sqlalchemy
from db.DBSettings import session
from sqlalchemy import Column


class KeyWordModel(Base):
    """
    キーワード検索
    key_wordのDBモデル
    """

    __tablename__ = 'key_word'

    id = Column('id', primary_key=True)
    match_word = Column('match_word')
    server_id = Column('server_id')


class MatchReply(Base):
    """
    キーワード検索
    match_replyのDBモデル
    """

    __tablename__ = 'match_reply'

    id = Column('id', primary_key=True)
    reply_word = Column('reply_word')
    match_id = Column('match_id')



def main():
    """
    メイン関数
    """
    # Config.set_config('/Users/usr0200618/study/bot/config.ini')
    uu = session.query(KeyWordModel).all()
    print(type(uu))
    for u in uu:
        print(u.server_id)


if __name__ == "__main__":
    main()

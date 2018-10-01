# coding: UTF-8

from DBManager import DBManager


def make_data_store(cursor, column):
    data_store = []
    for row in cursor:
        data_store.append(row[column])
    return data_store


class AcceptMessage:
    def __init__(self, db_obj):
        self.conn = db_obj.connector()
        self.mysql_connection = self.conn.cursor(dictionary=True)  # 結果を辞書型で受け取る

    def return_match_list(self):  # メソッドが呼ばれて１度しか呼ばれないので、initに入れるか関数化する
        column = 'match_word'
        cursor = self.mysql_connection
        cursor.execute("SELECT match_word "
                       "FROM key_word")
        return make_data_store(cursor, column)

    def return_reply_list(self, match_message):
        column = 'reply_word'
        cursor = self.mysql_connection
        match_message = ','.join(match_message)  # ['絶','ある']こんな感じで送られて来るので、文字列に
        cursor.execute("SELECT reply_word "
                       "FROM cmp_match_reply cmr "
                       "JOIN key_word kw "
                       "ON cmr.cmp_match_id = kw.id "
                       "WHERE match_word = %s",
                       (match_message,)
                       )
        return make_data_store(cursor, column)

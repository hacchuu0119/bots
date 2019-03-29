from db.querry_run.models.replay_models import *
from db.DBSettings import session
from db.querry_run.models.discord_info_models import ServersModel
from db.dbutil import *


class KeyWordDB(object):
    key_word_model = KeyWordModel
    server_list = ServersModel
    match_reply = MatchReply

    def match_word_all(self, server_id):
        match_word_list = session \
            .query(self.key_word_model.match_word) \
            .filter(self.key_word_model.server_id == server_id)
        return to_list(match_word_list)

    def match_word_server(self, server_name):
        """
        server_nameに登録されている、match_wordとIDを辞書型で返す
        {key_word: id}
        """
        match_word_list = session\
            .query(self.key_word_model.match_word)\
            .join(self.server_list, self.key_word_model.server_id == self.server_list.id)\
            .filter(self.server_list == server_name)

        return_dct = {}
        for obj in match_word_list:
            return_dct.update({obj.match_word: obj.id})

        return return_dct

    def pick_reply(self, match_id):
        reply_list = session.query(self.match_reply.reply_word).filter(self.match_reply.match_id == match_id)
        return to_list(reply_list)


if __name__ == "__main__":
    aa = KeyWordDB()
    print(aa.match_word_all(1))

    key_word_model = KeyWordModel
    server_list = ServersModel

    a = session.query(KeyWordModel)\
        .join(ServersModel, KeyWordModel.server_id == ServersModel.id)\
        .filter(ServersModel.name == "****").all()
    key_id_dct = {}
    for i in a:
        key_id_dct.update({i.match_word: i.id})
    print(key_id_dct)
    print(aa.pick_reply(3))

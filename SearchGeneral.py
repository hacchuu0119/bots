# coding: UTF-8

import AcceptMessage
import random
from db.querry_run.resmatch import KeyWordDB


def is_match(match_option, message):
    """
    match_optionのリストに全て当てはまった場合、Trueを返す
    :param match_option: key_wordのうちの1組のリスト ex) [x,y]
    :param message: ユーザの入力
    """
    for option_word in match_option:
        if option_word not in message:
            return False
    return True


def rand_pick(reply):
    print(f'reply: {reply}')
    return random.choice(reply)


class ReplyClass:
    match_word = []
    key_word = KeyWordDB()

    def __init__(self, message, server):
        self.accept_message = AcceptMessage.AcceptMessage()  # メソッドを初期化
        self.is_match = False
        self.reply_list = []
        self.match_message(message, server)

    def rand_pick_reply(self):
        print(f'reply: {self.reply_list}')
        return random.choice(self.reply_list)

    def match_message(self, get_comment, server_name):
        """
        DBからmatch_wordとmatch_idを引っ張ってきて、
        コメントとマッチしているか調べる
        マッチしてたら、そのmatch_idにマッチするリプライのリストを返す

        option = 候補
        """
        # サーバーに関連するマッチ候補を取ってくる
        match_option_dict = self.key_word.match_word_server(server_name)

        for matching_option_string in match_option_dict.keys():
            if is_match(matching_option_string.split(','), get_comment):
                # マッチした場合リプライのリストを返す
                self.reply_list = self.key_word.pick_reply(match_option_dict[matching_option_string])
                self.is_match = True

    class SearchReply:
        pass

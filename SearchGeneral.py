# coding: UTF-8

import SearchReply
import AcceptMessage


class ReplyClass:

    match_word = []

    def __init__(self):
        self.accept_message = AcceptMessage.AcceptMessage()  # メソッドを初期化
        self.match_list = self.accept_message.return_match_list()

    def bool_fulltext(self, get_comment):
        self.match_word, match_flag = SearchReply.match_message(get_comment, self.match_list)
        print(f'match_word: {self.match_word} match_flag: {match_flag}')
        return match_flag

    def matching_fulltext(self, get_comment):
        # match_word = SearchReply.match_message(get_comment, self.match_list)
        debug = f'get_comment: "{get_comment}" match_list: "{self.match_list}" match_word: {self.match_word}'
        print(debug)
        if self.match_word is None: return None
        reply = self.accept_message.return_reply_list(self.match_word)
        return SearchReply.rand_pick(reply)

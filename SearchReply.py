# coding: UTF-8

import this


class SearchReply():
    def __init__(self, comment, match_list, res_list):
        self.get_comment = comment
        self.get_match_list = match_list
        self.get_res_list = res_list

    def return_reply(self):
        accept_list = this.match_message(self.get_match_list)
        return this.return_reply(self, self.get_res_list, accept_list)

    # レスにマッチしたか判定
    # 返り値インデックス番号(AcceptMessageのインデックス番号)
    def match_message(self):
        for matching in self.get_match_list:
            for mat in matching:
                if mat in self.get_comment:
                    messe_num = self.get_match_list.index(matching)
                else:
                    messe_num = None
                    break
        return messe_num

    # match_messageで指定したindex番号を元に、返答を返す
    def return_reply(self, res_list, use_index):
        if use_index is None: return None
        return res_list[use_index][0]

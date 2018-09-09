# coding: UTF-8



class SearchReply:
    def __init__(self, comment, match_list, res_list):
        self.get_comment = comment
        self.get_match_list = match_list
        self.get_res_list = res_list

    def return_reply(self):
        accept_index = self.match_message(self.get_match_list)
        return self.pick_reply(self.get_res_list, accept_index)

    # レスにマッチしたか判定
    # 返り値インデックス番号(AcceptMessageのインデックス番号)
    def match_message(self, match_list):
        for matching in match_list:
            for mat in matching:
                if mat in self.get_comment:
                    messe_num = match_list.index(matching)
                    if matching.index(mat) == len(matching) - 1 and messe_num is not None:
                        return match_list.index(matching)
                else:
                    messe_num = None
                    break

        return messe_num

    # match_messageで指定したindex番号を元に、返答を返す
    def pick_reply(self, res_list, use_index):
        if use_index is None: return None
        return res_list[use_index][0]

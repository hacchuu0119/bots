# coding: UTF-8

import SearchReply
import AcceptMessage


class ReplyClass:

    def __init__(self, comment):
        self.get_comment = comment

    def full_text_match(self):
        acceptmessage = AcceptMessage.AcceptMessage()
        match_list = acceptmessage.return_match_list()
        reply_list = acceptmessage.return_reply_list()
        reply = SearchReply.SearchReply(self.get_comment, match_list, reply_list)
        return reply.return_reply()

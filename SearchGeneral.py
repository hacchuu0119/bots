# coding: UTF-8
from db.settings import Base, session
import random
from db.query.model.match_and_response_model import *


class MatchAndResponse:

    def __init__(self, user_response, guild_id):
        """
        :param user_response: ユーザのレス
        :param guild_id
        """
        self.bot_response_list = get_bot_response(user_response, guild_id)

    def rand_pick_reply(self):
        print(f'reply: {self.bot_response_list}')  # デバッグ
        return random.choice(self.bot_response_list)

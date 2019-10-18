# coding: UTF-8


from commands import custom_response, dice
from tools.BotUtil import BotUtil


def pin_help(command):
    if command == '/pin':
        return BotUtil.read_file_text('./resource/howtopin')
    elif command == '/dice' or command == 'ダイス':
        return BotUtil.read_file_text('./resource/howtodice')


def router(message):

    command = message.content.split()[0].replace("!", "", 1).replace("！", "", 1)

    if command == 'pin':
        return custom_response(message)

    elif command == 'dice' or command == 'ダイス' or command == 'ルーレット':
        return dice(message)


class Command:

    @classmethod
    def search(cls, message):
        return router(message)

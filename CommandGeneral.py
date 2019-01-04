# coding: UTF-8


from ConfigManager import Config
from commands.pin import pin_command
from commands.dice import dice_command
from tools.BotUtil import BotUtil


def pin_help(command):
    if command == '/pin':
        return BotUtil.read_file_text('./resource/howtopin')
    elif command == '/dice' or command == 'ダイス':
        return BotUtil.read_file_text('./resource/howtodice')


class Command:

    @classmethod
    def command_search(cls, message, user):
        if len(message.split()) > 1:  # 2以上なら引数あり
            command, args = message.replace('/', '', 1).split(' ', 1)
        elif message == 'ルーレット':
            command = 'ルーレット'
            args = 'ルーレット'
        else:
            return pin_help(message)

        if command == 'pin':
            pinfile_name = Config.get_config('PIN')['json']
            print(pinfile_name)
            return pin_command(args, pinfile_name)

        elif command == 'dice' or command == 'ダイス':
            return dice_command(args, user)
        elif command == 'ルーレット':
            return dice_command('ルーレット', user)

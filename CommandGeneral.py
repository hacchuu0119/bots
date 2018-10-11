from tools.JsonUtil import JsonUtil
from ConfigManager import Config
from tools.BotUtil import BotUtil


def pin_command(args):  # JsonUtilをインスタンス化した方がいいかも。何回も呼び出すし、ファイル名を2回入力してる
    pinfile_name = Config.get_config('PIN')
    pinfile_name = pinfile_name['json']
    print(args)

    pin_dict = JsonUtil.import_json(pinfile_name)
    if args.split()[0] == 'insert':
        key, value = args.split(' ', 1)[1].split(':', 1)  # insert a:b を a, bへ代入
        key = key.strip()
        value = value.lstrip()  # keyの前後の空白, value先頭の空白
        JsonUtil.update_json(pinfile_name, {key: value})
        return str(list(JsonUtil.import_json(pinfile_name).keys()))

    elif args == 'list':
        return str(list(pin_dict.keys()))

    elif args.split()[0] in pin_dict:
        return pin_dict[args]

    else:
        return '/pin は後ろに、キーワードか[insert, list]を打ってね！'


def pin_help(command):
    if command == '/pin':
        return BotUtil.read_file_text('./resource/howtopin')


class Command:

    @classmethod
    def command_search(cls, message):
        if len(message.split()) > 1:  # 2以上なら引数あり
            command, args = message.replace('/', '', 1).split(' ', 1)
        else:
            return pin_help(message)

        if command == 'pin':
            return pin_command(args)

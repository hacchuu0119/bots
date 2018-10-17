# coding: utf-8

from tools.JsonUtil import JsonUtil


def pin_command(args, file_path):  # JsonUtilをインスタンス化した方がいいかも。何回も呼び出すし、ファイル名を3回入力してる

    pin_dict = JsonUtil.import_json(file_path)
    if args.split()[0] == 'insert':
        key, value = args.split(' ', 1)[1].split(':', 1)  # insert a:b を a, bへ代入
        key = key.strip()
        value = value.lstrip()  # keyの前後の空白, value先頭の空白
        JsonUtil.update(file_path, {key: value})
        return str(list(JsonUtil.import_json(file_path).keys()))

    elif args.split()[0] == 'delete':
        keys = args.split()
        message = ''
        for i, key in enumerate(keys):
            if i == 0:
                continue
            message = message + JsonUtil.delete(file_path, key) + '\n'
        return message + '\n' + str(list(JsonUtil.import_json(file_path).keys()))

    elif args == 'list':
        return str(list(pin_dict.keys()))

    elif args.split()[0] in pin_dict:
        return pin_dict[args]

    else:
        return '/pin は後ろに、キーワードか[insert, list]を打ってね！'

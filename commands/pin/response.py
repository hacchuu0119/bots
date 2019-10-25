# coding: utf-8

import re
from db.query.model.match_and_response_model import insert_bot_response, get_bot_response, \
    check_existence_bot_response, delete_one_bot_response, delete_all_key_bot_response
import traceback


def insert_response(message, arguments):
    key, value = re.split('[ :　]', arguments, 1)

    try:
        insert_bot_response(key, message.guild.id, value, message.author.id)

    except Exception:
        traceback.print_exc()

        return f'{message.author.mention}さんの文字登録にしっぱいしました。。'

    return f'{message.author.mention}さんの、[{key}]を登録したよっ！'


def delete_all(key, guild_id):
    """
    [all, key]
    """
    if get_bot_response(key, guild_id):
        delete_all_key_bot_response(key, guild_id)
        return f'{key}の抹殺完了ぅ'

    else:
        return f'[{key}っていうマッチングワードはない！！\n' \
            f'ないのは削除できない！！！！'


def delete_one_pair(key, value, guild_id):
    if check_existence_bot_response(key, value, guild_id):
        delete_one_bot_response(key, value, guild_id)
        return f'[{key}: {value}]を削除完了。'

    else:
        return f'{key}:{value} は登録されてないよ？？\n' \
            f'もう一回しらべてみて！！'


def delete_key_only(key, guild_id):
    response_num = len(get_bot_response(key, guild_id))

    if response_num == 1:
        delete_all_key_bot_response(key, guild_id)
        return f'{key}の抹殺完了ぅ'

    elif response_num > 1:
        return f'[{key}]には複数の返事があるよ！！\n' \
            f'全部消したい場合は -> !res delete all {key}\n' \
            f'一つだけ消したい場合は -> !res delete {key} [消したい返答]\n' \
            f'って打ってね。やりなおし！！'

    else:
        return f'{key}っていう言葉は登録されてないよ？？ 大丈夫？'


def delete_response(message, arguments):
    """
    [all key] -> key全て削除
    [key] -> 複数の場合 -> 言ってvalueのリストを返す
    [key] -> 一つの場合 -> 削除
    [key, value] -> 一致するのを削除
    """
    arg_list = re.split('[ :　]', arguments, 2)
    if len(arg_list) == 2:
        if arg_list[0] == "all":  # [all, key]
            return delete_all(arg_list[1], message.guild.id)

        else:  # [key, value]
            return delete_one_pair(arg_list[0], arg_list[1], message.guild.id)

    elif len(arg_list) == 1:
        return delete_key_only(arg_list[0], message.guild.id)


def custom_response(message):
    try:
        command, mode, args = re.split('[ :　]', message.content, 2)

        if mode == 'insert':
            return insert_response(message, args)

        elif mode == 'delete':
            return delete_response(message, args)

    except ValueError:
        return f'{message.author.mention}さんの、コマンド処理に失敗したよ＞＜\n' \
            f'[!res help] って打って見てねっ'

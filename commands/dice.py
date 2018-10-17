# coding: UTF-8

import random
import re


def dice_command(args, user):
    args = args.strip()  # 引数の改行空白削除
    print(args)

    sf_check = False
    if '<' in args or len(args.split()) == 3:
        sf_check = True

    if 'd' in args or 'D' in args or 4 > len(args.split()) >= 2:  # [d][D][ ]で区切られてるなら分割する
        tmp = re.split('d|D| ', args)
        time = tmp[0]
        dice_type = tmp[1] + ' ' + tmp[2]
        if sf_check:
            dice_type, status = re.split('<=| |<', dice_type)
        res = dice_roll(int(time), int(dice_type))
        if len(res) > 1:
            res_message = str(user) + ' : (' + str(args) + ') -> ' + str(res) + ' -> ' + str(sum(res))
        else:
            res_message = str(user) + ' : (' + str(args) + ') -> ' + str(sum(res))

    elif not sf_check:
        return str(user) + ' さん、「' + str(args) + '」これ書き方間違ってるよ！\n下手に空白とか開けちゃだめだよー'
    if sf_check:
        if sum(res) <= int(status):
            return res_message + ' <= ' + status + ' = 成功☆'
        return res_message + ' > ' + status + ' = 失敗'
    return res_message


def dice_roll(time, dice_type):
    res_list = []
    for i in range(time):
        res_list.append(random.randrange(dice_type))
    return res_list

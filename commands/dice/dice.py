# coding: UTF-8

import random
import re


def dice(message):

    if 'ルーレット' in message.content:
        args = '1d100'
    else:
        args = message.content.replace("　", " ", 1).split()[1]

    if 'd' in args\
            or 'D' in args \
            or len(args.split()) is 2:  # [d][D][ ]で区切られてるなら分割する

        tmp = re.split('d|D| ', args)
        roll_times = tmp[0]
        dice_type = tmp[1]

        dice_result = dice_roll(int(roll_times), int(dice_type))
        if len(dice_result) >= 1:
            return f'{message.author.mention} :({roll_times}D{dice_type})' \
                f' ->[{", ".join(map(str, dice_result))}]' \
                f' -> {str(sum(dice_result))}'
        else:
            return f'{message.author.mention}さんのDICE実行に失敗しました・・。: {args}'


def dice_roll(roll_times, dice_type):
    res_list = []
    for i in range(roll_times):
        res_list.append(random.randrange(1, dice_type))
    return res_list

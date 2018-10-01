# coding: UTF-8

import random


# レスにマッチしたか判定
# このメソッドキモい。変えたい
def match_message(get_comment, match_list):
    for matching in match_list:
        matching = matching.split(',')
        for mat in matching:
            if mat in get_comment:
                messe_num = match_list.index(','.join(matching))
                if matching.index(mat) == len(matching) - 1 and messe_num is not None:
                    print()
                    return matching, True
            else:
                break

    return [], False


def rand_pick(reply):
    print(f'reply: {reply}  random: {random.randrange(len(reply))}')
    return reply[random.randrange(len(reply))]

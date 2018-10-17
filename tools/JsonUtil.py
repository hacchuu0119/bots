# coding: UTF-8

import json


def dump_json(file_name, new_dict):
    file_obj = open(file_name, 'w')
    json.dump(new_dict, file_obj, ensure_ascii=False, )
    file_obj.close()


class JsonUtil:

    @classmethod
    def update(cls, file_name, new_add):
        old_dict = JsonUtil.import_json(file_name)
        old_dict.update(new_add)
        dump_json(file_name, old_dict)

    @classmethod
    def import_json(cls, file_name):
        file_obj = open(file_name, 'r')
        json_dict = json.load(file_obj)
        file_obj.close()
        return json_dict

    @classmethod
    def delete(cls, file_name, delete_key):
        old_dict = JsonUtil.import_json(file_name)
        if delete_key in old_dict:
            old_dict.pop(delete_key)
            dump_json(file_name, old_dict)
            return delete_key + ' を消したよ。'
        else:
            return '『 ' + delete_key + '』っていうkeyなんてないよ？？'

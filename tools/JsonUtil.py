import json


def dump_json(file_name, new_dict):
    file_obj = open(file_name, 'w')
    json.dump(new_dict, file_obj, ensure_ascii=False, )
    file_obj.close()


class JsonUtil:

    @classmethod
    def update_json(cls, file_name, new_add):
        old_dict = JsonUtil.import_json(file_name)
        old_dict.update(new_add)
        dump_json(file_name, old_dict)

    @classmethod
    def import_json(cls, file_name):
        file_obj = open(file_name, 'r')
        json_dict = json.load(file_obj)
        file_obj.close()
        return json_dict

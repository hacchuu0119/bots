class BotUtil:

    @classmethod
    def read_file_text(cls, file_path):
        with open(file_path) as read_file:
            read_text = read_file.read()
        return read_text

def command_search(message):
    command, args = message.replace('/', '').split(' ', 1)

    if command == 'pin':
        return pin_command(args)


def pin_command(args):
    dict = {'ハルヤマ': 'https://www.youtube.com/watch?v=2vZ4dryA2as&feature=share'}

    if args == 'list':
        return str(list(dict.keys()))
    elif args in dict:
        return dict[args]

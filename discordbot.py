# coding: UTF-8

import discord
import argparse
from CommandCTL import Command
from CustomResponse import CustomResponse
from ConfigManager import Config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help='Designate the access token to connect to your discord bot')
    parser.add_argument('-c', '--config', help='Enter config file with path')
    args = parser.parse_args()

    # Config(args.config)
    Config.set_config(args.config)

    client = discord.Client()  # 接続に使用するオブジェクト

    # 起動時に通知してくれる処理
    @client.event
    async def on_ready():
        print('ログインしました')

    @client.event
    async def on_message(message):
        if client.user == message.author: return  # 発言ユーザが自分の場合return
        print(f'{message.author}: {message.content} :{message.author.mention}')
        print(type(message.channel))

        print(message.author.id)

        if message.content.startswith('!') or message.content.startswith('！'):
            reply = Command.search(message)

            await message.channel.send(reply)
            return

        bot_response = CustomResponse(message.content, message.guild.id)  # searchGeneralの初期化

        if bot_response.bot_response_list:
            bot_res = bot_response.rand_pick_reply()
            await message.channel.send(bot_res)

    # botの接続と起動
    client.run(args.token)


if __name__ == '__main__':
    main()

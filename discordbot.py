# coding: UTF-8


import SearchGeneral
import discord  # インストールした discord.py
import asyncio
import argparse
from DBManager import DBManager
import UserGeneral
from CommandGeneral import Command
from ConfigManager import Config

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', help='Designate the access token to connect to your discord bot')
parser.add_argument('-c', '--config', help='Enter config file with path')
args = parser.parse_args()

# Config(args.config)
Config.set_config(args.config)
DBManager.set_db()

client = discord.Client()  # 接続に使用するオブジェクト


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')
    UserGeneral.update_user_db(client.get_all_members())
    # for user in client.get_all_members():


@client.event
async def on_message(message):
    if client.user == message.author: return  # 発言ユーザが自分の場合return
    print(f'{message.author}: {message.content} :{message.author.mention}')
    if message.content.startswith('/') or message.content.startswith('ダイス') or message.content.startswith('ルーレット'):
        reply = Command.command_search(message.content, message.author)

        await client.send_message(message.channel, reply)
        return

    bot_reply = SearchGeneral.ReplyClass()  # searchGeneralの初期化

    if bot_reply.bool_fulltext(message.content):
        reply = bot_reply.matching_fulltext(message.content)

        await client.send_message(message.channel, reply)

    if message.content.startswith('/waku'):
        reply = 'waku'
        await client.send_message(message.channel, reply)

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    if client.user.id in message.content:
        # 自分用
        if message.author.mention == "<@330411083980603394>":
            reply = f'お呼びですか、{message.author.mention} 様！'
        # シエルさん
        elif message.author.mention == "<@294059343068921857>":
            reply = f'(何言ってんだ、{message.author.mention} ？？)'
        #
        elif message.author.mention == "<@301692231775944716>":
            reply = f'あ、{message.author.mention}だ！ かわいい！SS撮ろ！'
        else:
            reply = f'{message.author.mention}さん、なにかご用ですか？'
        await client.send_message(message.channel, reply)


# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run(args.token)

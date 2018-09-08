# coding: UTF-8

import SearchGeneral
import discord  # インストールした discord.py
import asyncio

client = discord.Client()  # 接続に使用するオブジェクト


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if '絶' in message.content and 'ある' in message.content or '今日' in message.content or 'する':
        reply1 = '有りますよ！！'
        await client.send_message(message.channel, reply1)

    if 'シーバー' in message.content:
        reply = 'しばさん頑張って！'
        await client.send_message(message.channel, reply1)

    sarch = SearchGeneral.ReplyClass(message.content, )

    if message.content.startswith('/neko'):
        reply = 'にゃーん'
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
        print(message.author.mention)
        if (message.author.mention == "<@330411083980603394>"):
            reply = f'お呼びですか、{message.author.mention} 様: {message.content}！'

        elif (message.author.mention == "<@294059343068921857>"):
            reply = f'(何言ってんだ、{message.author.mention} ？？)'
        else:
            reply = f'{message.author.mention}さん、なにかご用ですか？ {client.user}'
        print(reply)
        await client.send_message(message.channel, reply)


# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NDg3NjEwODY5MTE1NzgxMTIx.DnQLQw.M0Fg5EOxeDsWvOtda7dq2ebQAgQ')

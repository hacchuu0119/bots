import discord # インストールした discord.py

client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
        
    if message.content.startswith('/waku'):
        reply = 'waku'
        await client.send_message(message.channel, reply)

    if client.user.id in message.content:
        print(message.author.mention)
        if (message.author.mention == "<@330411083980603394>"):
            reply = f'{message.author.mention} 様！好きです！'

        elif(message.author.mention == "<@294059343068921857>"):
            reply = f'(何言ってんだ、{message.author.mention} ？？)'
        else:
            reply = f'{message.author.mention} 呼んだ？？'
        print(reply)
        echo_method(reply)
        await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NDg3NjEwODY5MTE1NzgxMTIx.DnQLQw.M0Fg5EOxeDsWvOtda7dq2ebQAgQ')

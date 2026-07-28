@client.event...
mainChannel = client.get_server(constants.Settings.mainServerID).get_channel(
    constants.Settings.mainChannelId)
logsChannel = client.get_server(constants.Settings.mainServerID).get_channel(
    constants.Settings.logsChannelId)
print('Logged in !')
await asyncio.sleep(0.1)
hello = False
if datetime.now().strftime('%H') == '00' or set(sys.argv) & set(['refresh']):
message = await client.send_message(mainChannel,
    '<:empty:317951266355544065> Updating stats ...')
print('Ready !')
print('Refreshing users stats ...')
await client.edit_message(message,
    '<:xmark:317951256889131008> Updating stats ... Fail !')
if not set(sys.argv) & set(['dev']):
if set(sys.argv) & set(['online']) and hello == False:
refresh_all_pp_stats()
await client.send_message(mainChannel,
    '<:online:317951041838514179> Uso!<:Bot:317951180737347587> is now online !'
    )
await client.send_message(mainChannel,
    '<:online:317951041838514179> Uso!<:Bot:317951180737347587> is now online !'
    )
if set(sys.argv) & set(['dev']):
print(' - Done')
await client.change_presence(status=discord.Status('online'), game=discord.
    Game(name='Osu !'))
await client.change_presence(status=discord.Status('online'), game=discord.
    Game(name='Osu !'))
await client.change_presence(status=discord.Status('idle'), game=discord.
    Game(name='Dev mode'))
await client.edit_message(message,
    '<:check:317951246084341761> Updating stats ... Done !')
hello = True

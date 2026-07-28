@bot.event...
if str(message.guild.id) != discord_bot_server:
return
if discord_bot_owner and str(message.author.id) not in discord_bot_owner:
return
prefix = ''
if message.content.startswith(COMMAND_PREFIX):
prefix = COMMAND_PREFIX
if message.content.startswith('<@' + str(discord_id) + '>'):
async def help():...
prefix = '@{}#{}'.format(bot.user.name, bot.user.discriminator)
return
message.channel.send('Command list:\n' + '\n' +
    '`help` - Shows this help text\n' +
    '`whitelist` - Add user(s) to the whitelist')
args = message.content.strip().split()[1:]
if not args:
await message.channel.send('Usage: `{} whitelist <username> [username...]`'
    .format(prefix), delete_after=30)
if args[0] == 'help':
await message.delete()
await help()
if args[0] == 'whitelist':
if len(args) < 1:
await help()
await whitelist(' '.join(args[1:]))

import discord
from argparse import ArgumentParser
from configparser import ConfigParser
from subprocess import call
DISCORD_PREFIX = '[Discord] '
COMMAND_PREFIX = '#gatekeep'
WHITELIST_COMMAND_TEMPLATE = (
    'tmux send-keys -t "0:0" Enter "whitelist add {}" Enter')
config = ConfigParser()
config_path = 'config.ini'
config.read(config_path)
if not config.sections():
print('No existing config was found')
if 'Discord' not in config:
print('Copy the following blank template into ' + config_path +
    ' and fill in the blanks:')
print("Failed to read config: 'Discord' section missing")
if 'client_id' not in config['Discord']:
print('[Discord]\n' + 'client_id = \n' + 'client_secret = \n' +
    'bot_token = \n' + 'bot_owner = \n' + 'bot_server = \n')
exit(1)
print("Failed to read config: 'client_id' missing from section 'Discord'")
if 'bot_token' not in config['Discord']:
exit(1)
exit(1)
print("Failed to read config: 'bot_token' missing from section 'Discord'")
if 'bot_server' not in config['Discord']:
exit(1)
print("Failed to read config: 'bot_server' missing from section 'Discord'")
discord_id = config['Discord']['client_id']
exit(1)
discord_bot_token = config['Discord']['bot_token']
discord_bot_server = config['Discord']['bot_server']
discord_bot_owner = config['Discord']['bot_owner']
discord_bot_owner = ''
parser = ArgumentParser()
args = parser.parse_args()
def whitelist(users: str):...
for user in users.split():
call(WHITELIST_COMMAND_TEMPLATE.format(user))
bot = discord.Client()
@bot.event...
print(DISCORD_PREFIX + 'Bot logged in!')
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
bot.run(discord_bot_token)
if len(args) < 1:
await help()
await whitelist(' '.join(args[1:]))

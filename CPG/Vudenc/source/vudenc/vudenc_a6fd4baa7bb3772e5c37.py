import discord, yaml, vroll, pgsql, re
import texttable as tt
from discord.ext import commands
config = yaml.safe_load(open('config.yaml'))
token = config['token']
chan_whitelist = config['chan_whitelist']
pg_connection = config['pg_connection']
role_whitelist = config['role_whitelist']
permission_error_message = config['permission_error_message']
quest_tier_whitelist = config['quest_tiers']
pgsql.create_tables(pg_connection)
description = """
Vishnu, a multipurpose D&D bot.
"""
bot = commands.Bot(command_prefix='!', description=description)
"""
Role whitelisting function
"""
def whitelist_check(ctx):...
for x in role_whitelist:
if x in [y.id for y in ctx.message.author.roles]:
"""
QUEST-RELATED COMMANDS
"""
return True
return False
@bot.command()...
"""docstring"""
if whitelist_check(ctx):
if quest_tier in quest_tier_whitelist:
await ctx.send(permission_error_message)
if len(desc) < 100:
await ctx.send(
    'Error: The quest tier you specified is invalid. The valid quest tiers are: '
     + ', '.join(quest_tier_whitelist) + '. You specified: ' + quest_tier)
@bot.command()...
quest_desc = ' '.join(desc)
await ctx.send(
    'Error: Your description is too long. The maximum allowed characters is 100, you had '
     + str(len(desc)))
"""docstring"""
creator = str(ctx.author)
if whitelist_check(ctx):
pgsql.import_quest_data(pg_connection, quest_tier, quest_desc, creator)
pgsql.delete_quest(pg_connection, quest_id)
await ctx.send(permission_error_message)
print('Tier {} quest added by {}. Description: {}'.format(quest_tier, str(
    ctx.author), quest_desc))
await ctx.send('Quest with ID ' + quest_id + ' deleted.')
@bot.command()...
await ctx.send('Tier {} quest added by {}. Description: {}'.format(
    quest_tier, str(ctx.author), quest_desc))
"""docstring"""
if whitelist_check(ctx):
pgsql.complete_quest(pg_connection, quest_id, True)
await ctx.send(permission_error_message)
@bot.command()...
"""docstring"""
if whitelist_check(ctx):
pgsql.complete_quest(pg_connection, quest_id, False)
await ctx.send("You don't have permission to use this command")
@bot.command()...
"""docstring"""
command = ' '.join(map(str, args))
idsearch = 'id=([\\d])'
tiersearch = 'tier=([^\\s]+)'
creatorsearch = 'creator=([^\\s]+)'
idformat = ''
tierformat = ''
creatorformat = ''
if re.search(idsearch, command) is not None:
idmatch = re.search(idsearch, command).group(1)
if re.search(tiersearch, command) is not None:
idformat = 'AND id = {}'.format(idmatch)
tiermatch = re.search(tiersearch, command).group(1)
if re.search(creatorsearch, command) is not None:
tierformat = "AND tier = '{}'".format(tiermatch)
creatormatch = re.search(creatorsearch, command).group(1)
query = (
    """
    SELECT id, tier, creator, description FROM quests
    WHERE completed = 'f'
    {}
    {}
    {};
    """
    .format(idformat, tierformat, creatorformat))
creatorformat = "AND creator = '{}'".format(creatormatch)
query_return = pgsql.retrieve_quest_data(pg_connection, query)
tab = tt.Texttable()
headings = ['ID', 'TIER', 'CREATOR', 'DESCRIPTION']
tab.header(headings)
for x in range(0, len(query_return), 5):
for row in query_return[x:x + 5]:
"""
DICE COMMANDS
"""
tab.add_row(row)
s = tab.draw()
@bot.command()...
print(len(query_return))
"""docstring"""
await ctx.send('```' + s + '```')
if chan_whitelist is None:
tab.reset()
for x in args:
if ctx.channel.id in chan_whitelist:
print('!roll command recieved in channel ID ' + str(ctx.channel.id))
@bot.event...
for x in args:
await ctx.send(vroll.roll(x))
print('{0.user} connected to server'.format(bot))
print('!roll command recieved in channel ID ' + str(ctx.channel.id) +
    ' by user ' + str(ctx.author))
print('Whitelisted channel IDs are: ' + str(chan_whitelist))
await ctx.send(vroll.roll(x))
print('Whitelisted role IDs are: ' + str(role_whitelist))
bot.run(token)

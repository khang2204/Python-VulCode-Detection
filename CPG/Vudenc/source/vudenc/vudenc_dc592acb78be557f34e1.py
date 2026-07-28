@bot.command()...
"""docstring"""
if whitelist_check(ctx):
if quest_tier in quest_tier_whitelist:
await ctx.send(permission_error_message)
if len(desc) < 100:
await ctx.send(
    'Error: The quest tier you specified is invalid. The valid quest tiers are: '
     + ', '.join(quest_tier_whitelist) + '. You specified: ' + quest_tier)
quest_desc = ' '.join(desc)
await ctx.send(
    'Error: Your description is too long. The maximum allowed characters is 100, you had '
     + str(len(desc)))
creator = str(ctx.author)
pgsql.import_quest_data(pg_connection, quest_tier, quest_desc, creator)
print('Tier {} quest added by {}. Description: {}'.format(quest_tier, str(
    ctx.author), quest_desc))
await ctx.send('Tier {} quest added by {}. Description: {}'.format(
    quest_tier, str(ctx.author), quest_desc))

@bot.command()...
"""docstring"""
if chan_whitelist is None:
for x in args:
if ctx.channel.id in chan_whitelist:
print('!roll command recieved in channel ID ' + str(ctx.channel.id))
for x in args:
await ctx.send(vroll.roll(x))
print('!roll command recieved in channel ID ' + str(ctx.channel.id) +
    ' by user ' + str(ctx.author))
await ctx.send(vroll.roll(x))

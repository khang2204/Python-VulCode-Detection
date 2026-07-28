@bot.command()...
"""docstring"""
if whitelist_check(ctx):
pgsql.complete_quest(pg_connection, quest_id, False)
await ctx.send("You don't have permission to use this command")

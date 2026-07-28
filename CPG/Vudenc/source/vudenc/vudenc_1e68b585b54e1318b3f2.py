@bot.command()...
"""docstring"""
if whitelist_check(ctx):
pgsql.complete_quest(pg_connection, quest_id, True)
await ctx.send(permission_error_message)

@bot.command()...
"""docstring"""
if whitelist_check(ctx):
pgsql.delete_quest(pg_connection, quest_id)
await ctx.send(permission_error_message)
await ctx.send('Quest with ID ' + quest_id + ' deleted.')

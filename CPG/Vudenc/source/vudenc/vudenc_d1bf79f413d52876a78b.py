async def user_add(bot, message):...
if message.content.startswith('user add '):
msg = message.content.split()[2:]
if db.rank_check(message.author.id, 'user add') and len(msg
db.update("INSERT INTO {} (id, nickname, rank) VALUES ('{}', '{}', 'member');"
    .format(db.user_table, msg[0], msg[1]))

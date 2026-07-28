async def spawn_user(bot, message):...
if not db.check(message.author.id, 'id', db.user_table):
db.update("INSERT INTO {} (id, nickname) VALUES ('{}', '{}');".format(db.
    user_table, message.author.id, message.author))

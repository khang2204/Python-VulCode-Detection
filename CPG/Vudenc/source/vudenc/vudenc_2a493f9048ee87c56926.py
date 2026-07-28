async def on_message(self, message):...
server = message.server
author = message.author
channel = message.channel
c = self.database.cursor()
c.execute('SELECT EXISTS(SELECT 1 FROM USER WHERE id=' + str(author.id) +
    ' collate nocase) LIMIT 1')
if c.fetchone()[0] == 0:
c.execute("INSERT INTO USER VALUES ('" + author.name + "'," + author.id +
    ",'" + str(author.bot) + "','" + author.avatar + "','" + str(author.
    created_at) + "')")
c.execute('SELECT EXISTS(SELECT 1 FROM SERVERS WHERE id=' + str(server.id) +
    ' collate nocase) LIMIT 1')
if c.fetchone()[0] == 0:
c.execute("INSERT INTO SERVERS VALUES ('" + server.name + "'," + server.id +
    ',' + server.owner.id + ')')
print(message.edited_timestamp)
sql_command = (message.id + ",'" + str(message.edited_timestamp) + "','" +
    str(message.timestamp) + "','" + str(message.tts) + "','" + str(message
    .author.name) + "'," + str(message.author.id) + ",'" + message.content +
    "'," + message.server.id + ',' + message.channel.id)
print(sql_command)
c.execute('INSERT INTO MESSAGE VALUES (' + sql_command + ')')
self.database.commit()

def link_user(discordId, osuName, osuId, rank):...
result = ''
print('Linking : discordId : ' + str(discordId) + ', osuName : ' + osuName +
    ', osuId : ' + str(osuId) + ' to Database.', end=' ')
conn = sqlite3.connect(databasePath)
cursor = conn.cursor()
cursor.execute('SELECT * FROM users WHERE discordId = ' + str(discordId))
if len(cursor.fetchall()) == 0:
cursor.execute(
    """
		INSERT INTO users (discordId, osuName, osuId, rank) 
		VALUES (?, ?, ?, ?)
		"""
    , (discordId, osuName, osuId, rank))
cursor.execute("UPDATE users SET osuName = '" + osuName + "', osuId = " +
    str(osuId) + ", rank = '" + rank + "' WHERE discordId = " + str(discordId))
conn.commit()
conn.commit()
print('Added')
print('Updated')
result = 'linked'
result = 'updated'
conn.close()
return result

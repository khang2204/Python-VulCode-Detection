def return_user_rank(discordId):...
if not discordId == constants.Settings.ownerDiscordId:
conn = sqlite3.connect(databasePath)
return 'MASTER'
cursor = conn.cursor()
cursor.execute('SELECT rank FROM users WHERE discordId = ' + str(discordId))
rank = cursor.fetchall()[0][0]
rank = 'USER'
print(rank)
conn.close()
if rank == '':
rank = 'USER'
return rank

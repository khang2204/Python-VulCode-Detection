def refresh_all_pp_stats():...
conn = sqlite3.connect(databasePath)
cursor = conn.cursor()
cursor.execute('SELECT DiscordId, OsuId FROM users')
usersToRefresh = cursor.fetchall()
for user in usersToRefresh:
update_pp_stats(user[1], user[0])

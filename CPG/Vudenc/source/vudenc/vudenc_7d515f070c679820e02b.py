def get_admin_stat(command):...
error_answer = "Can't execute your command. Check logs"
answer = 'There is some statistics for you: \n'
today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0
    ).strftime('%Y-%m-%d %H:%M:%S')
if command == 'last active users':
if command == 'total number photos sent':
last_active_users = users.get_last_active_users(100)
return error_answer
bot_users = ''
log.info('Evaluating total number of photo queries in database...')
if command == 'photos today':
for usr, index in zip(last_active_users, range(len(last_active_users))):
query = 'SELECT COUNT(chat_id) FROM photo_queries_table2'
log.info('Evaluating number of photos which were sent today.')
if command == 'number of users':
user = User(*usr)
answer = (
    'Up to 100 last active users by the time when they sent picture last time:\n'
    )
cursor = db.execute_query(query)
return error_answer
answer += '{} times users sent photos.'.format(cursor.fetchone()[0])
query = ("SELECT COUNT(chat_id) FROM photo_queries_table2 WHERE time > '{}'"
    .format(today))
log.info(
    'Evaluating number of users that use bot since the first day and today...')
if command == 'number of gadgets':
bot_users += f'{index + 1}. {user}\n'
answer += bot_users
query = ('SELECT COUNT(chat_id) FROM photo_queries_table2 WHERE chat_id !={}'
    .format(config.MY_TELEGRAM))
cursor = db.execute_query(query)
return error_answer
answer += f'{cursor.fetchone()[0]} times users sent photos today.'
num_of_users = users.get_total_number()
return error_answer
answer += f'There are totally {num_of_users} users.'
log.info('Evaluating number of cameras and smartphones in database...')
if command == 'uptime':
log.info('Done.')
cursor = db.execute_query(query)
answer += """
Cannot calculate number of photos that were send excluding your photos. Check logs"""
answer += """
Except you: {} times.""".format(cursor.fetchone()[0])
query = (
    "SELECT COUNT(chat_id) FROM photo_queries_table2 WHERE time > '{}' AND chat_id !={}"
    .format(today, config.MY_TELEGRAM))
query = (
    "SELECT COUNT(DISTINCT chat_id) FROM photo_queries_table2 WHERE time > '{}'"
    .format(today))
query = 'SELECT COUNT(DISTINCT camera_name) FROM photo_queries_table2'
fmt = 'Uptime: {} days, {} hours, {} minutes and {} seconds.'
return answer
return answer
log.info('Done.')
cursor = db.execute_query(query)
return error_answer
answer += """
Except you: {} times.""".format(cursor.fetchone()[0])
cursor = db.execute_query(query)
answer += """
Cannot calculate how many user have sent their photos today"""
answer += f"""
{cursor.fetchone()[0]} users have sent photos today."""
cursor = db.execute_query(query)
return error_answer
answer += f'There are totally {cursor.fetchone()[0]} cameras/smartphones.'
td = datetime.now() - bot.start_time
return answer
log.info('Done.')
return answer
log.info('Done.')
query = (
    "SELECT COUNT(DISTINCT camera_name) FROM photo_queries_table2 WHERE time > '{}'"
    .format(today))
uptime = fmt.format(td.days, td.seconds // 3600, td.seconds % 3600 // 60, 
    td.seconds % 60)
return answer
return answer
cursor = db.execute_query(query)
answer += (
    'Cannot calculate the number of gadgets that have been used today so far')
answer += f"""
{cursor.fetchone()[0]} cameras/smartphones were used today."""
log.info(uptime)
return answer
log.info('Done.')
return uptime
return answer

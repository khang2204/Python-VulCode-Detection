async def ex_me(dclient, channel, mention, con, con_ex, author_id, a,...
a = a.split(' ')
if len(a) >= 2:
time = a[0].lower()
await dclient.send_message(channel,
    '{}, **USAGE:** {}remindme <time> <message...>'.format(mention, cmd_char))
msg = ''
print('')
for i in range(1, len(a)):
msg += a[i] + ' '
if 'd' in time or 'h' in time or 'm' in time or 's' in time or ',' in time:
date = get_date(time)
await dclient.send_message(channel,
    '{}, The time must be in #time format (ex: 1h or 2h,5m).'.format(
    mention, cmd_char))
con_ex.execute(
    "INSERT INTO reminder (type, channel, message, date) VALUES ('0', {}, '{}', '{}');"
    .format(author_id, msg, date.strftime('%Y-%m-%d %X')))
await dclient.send_message(channel,
    '{}, error when trying to add info to database! Please notifiy the admins!'
    .format(mention))
con.commit()
print('[{}]: {} - {}'.format(strftime('%b %d, %Y %X', localtime()),
    'SQLITE', 'Error when trying to insert data: ' + e.args[0]))
await dclient.send_message(channel, '{}, will remind you.'.format(mention))
log_file.write('[{}]: {} - {}\n'.format(strftime('%b %d, %Y %X', localtime(
    )), 'SQLITE', 'Error when trying to insert data: ' + e.args[0]))

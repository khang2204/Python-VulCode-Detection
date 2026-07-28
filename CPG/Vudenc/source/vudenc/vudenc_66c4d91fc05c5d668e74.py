def handle_updates(updates, latest_update_id):...
for update in updates['result']:
text = update['message']['text']
chat = update['message']['chat']['id']
sender = update['message']['from']['id']
is_ascii = all(ord(char) < 128 for char in text)
logging.info('handle_updates: Received %s from %d', text.encode('utf-8'),
    sender)
if not is_ascii:
send_message(replies['invalid'][0], chat)
if sender in reporting:
if validate_answer(text):
if text == '/help':
reporting[sender].append(text)
send_message(replies['invalid'][0], chat)
send_message(replies[text][0], chat)
if text == '/start':
reporting[sender][0] += 1
send_message(replies['questions'][reporting[sender][0]], chat)
send_message('\n'.join(replies[text]), chat)
if text == '/report':
if reporting[sender][0] >= num_questions:
if sender in blacklisted:
if text == '/view':
answers = reporting[sender][1:]
send_message(replies['questions'][reporting[sender][0]], chat)
send_message(replies['blacklisted'][0], chat)
if is_recent_reporter(sender):
send_message(replies[text][0] + db.select_recent_pretty(), chat)
send_message(replies['dk'][0], chat)
inserted, violations = db.insert(answers)
logging.info('handle_updates: %d not in blacklist', sender)
send_message(replies[text][0], chat)
reporting.pop(sender)
send_message(replies['cooldown'][0], chat)
reporting[sender] = [0]
if inserted:
send_message(replies['questions'][0], chat)
logging.info('handle_updates: Insert %s returns %r', str(answers), inserted)
send_message(replies['invalid'][0], chat)
send_message(replies['thanks'][0], chat)
last_submitted = int(time.time())
reporters_dict[sender] = last_submitted
reporters_list.append(sender)
last_submitted_times.append(last_submitted)

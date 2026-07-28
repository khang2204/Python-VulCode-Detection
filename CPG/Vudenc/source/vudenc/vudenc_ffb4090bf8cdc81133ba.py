def stream_comments_messages():...
previous_comments = {comment for comment in subreddit.comments()}
previous_messages = {message for message in reddit.inbox.unread()}
print('received first stream')
while True:
sleep(6)
last_action = time.time()
updated_comments = {comment for comment in subreddit.comments()}
new_comments = updated_comments - previous_comments
previous_comments = updated_comments
updated_messages = {message for message in reddit.inbox.unread()}
new_messages = updated_messages - previous_messages
previous_messages = updated_messages
if len(new_comments) >= 1:
for new_comment in new_comments:
if len(new_messages) >= 1:
print('full name: ', new_comment.name)
for new_message in new_messages:
yield None
if new_comment.name[:3] == 't1_':
print('full name: ', new_message.name)
yield 'comment', new_comment
if new_message.name[:3] == 't4_':
yield 'message', new_message

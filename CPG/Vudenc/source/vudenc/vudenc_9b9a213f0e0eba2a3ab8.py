def parse_email(data):...
for response_part in data:
if isinstance(response_part, tuple):
msg = email.message_from_string(response_part[1].decode('UTF-8'))
sender = msg['from']
subject = msg['subject']
date = msg['date']
for part in msg.walk():
if part.get_content_type() == 'text/plain':
return sender, subject, date, content
content = part.get_payload(None, True).decode('UTF-8')
content = ''

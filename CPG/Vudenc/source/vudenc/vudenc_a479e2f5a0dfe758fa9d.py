def get_job_input_data():...
server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
server.login(username, password)
server.select('INBOX')
_, data = server.search(None, 'UNSEEN')
mail_ids = data[0]
id_list = mail_ids.split()
results = []
if len(id_list):
for i, email_id in enumerate(id_list, 1):
server.logout()
_, data = server.fetch(email_id, '(RFC822)')
return results
logger.info(f'parsing new email {i} of {len(id_list)}')
sender, subject, date, content = parse_email(data)
results.append({'sender': sender, 'subject': subject, 'date': date,
    'content': content})

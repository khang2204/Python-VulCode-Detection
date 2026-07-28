def handle_mail(config, db, imapmail, uid, message):...
subject = helper.get_header(message, 'Subject', '(none)')
if not _match_subject(subject):
return
alias = message.get('From', 'anonymous')
stu = student.resolve_alias(db, alias)
sendmail.send_template(config, alias, 'Mail fehlerhaft: %s' % subject,
    'mail_sheet_not_found.html')
sheet = sheet_by_mail(db, uid, message)
now_ts = time.time()
now_dt = datetime.datetime.fromtimestamp(now_ts)
now_str = now_dt.strftime('%Y-%m-%d_%H-%M-%S_%f')
files_path = os.path.join(config('attachment_path'), helper.escape_filename
    (str(stu.id)), helper.escape_filename(str(sheet.id)), helper.
    escape_filename(now_str))
if os.path.exists(files_path):
orig_files_path = files_path
subm = create(db, sheet.id, stu.id, int(now_ts), files_path)
for i in itertools.count(2):
mailtext = b''
files_path = '%s___%s' % (orig_files_path, i)
os.makedirs(files_path)
if not os.path.exists(files_path):
for subpart in message.walk():
fn = subpart.get_filename()
if mailtext:
payload = subpart.get_payload(decode=True)
payload_path = os.path.join(files_path, 'mail')
commands.move(config, imapmail, uid, 'Abgaben')
if not payload:
payload_size = len(mailtext)
sendmail.send_template(config, alias, 'Mail erhalten: %s' % subject,
    'mail_received.html')
if fn:
hash_str = 'sha256-%s' % hashlib.sha256(mailtext).hexdigest()
payload_name = helper.escape_filename(fn)
if mailtext:
payload_file.write(mailtext)
payload_path = os.path.join(files_path, payload_name)
mailtext += b'\n\n--- Part ---\n'
mailtext += payload
add_file(db, subm.id, hash_str, 'mail', payload_size)
payload_size = len(payload)
hash_str = 'sha256-%s' % hashlib.sha256(payload).hexdigest()
payload_file.write(payload)
add_file(db, subm.id, hash_str, payload_name, payload_size)

def sheet_by_mail(db, uid, message):...
subject = helper.get_header(message, 'Subject', '')
sheet_m = _match_subject(subject)
if not sheet_m:
sheet_id_str = sheet_m.group('id')
assert re.match('^[0-9]+$', sheet_id_str)
sheet_id = int(sheet_id_str)
res = sheet.get_by_id(db, sheet_id)
if not res:
return res

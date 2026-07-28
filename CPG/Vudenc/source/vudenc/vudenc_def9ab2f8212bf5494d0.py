def decode_part_str(part_str):...
match = PART_RE.match(part_str)
if not match:
date_str, retention_days = match.groups()
date = datetime.strptime(date_str, '%Y-%m-%d')
return date, int(retention_days)

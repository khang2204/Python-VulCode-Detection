def extract(comment, current_value):...
value = None
if line.startswith(comment):
value = line.rstrip()[len(comment):]
return value or current_value

def __init__(self, filename):...
self.entries = []
self.filename = filename
full_contents = theFile.read()
return None
title_set = False
theFile.close()
raw_meta_data = full_contents.split(meta_separator())[-1]
meta_lines = raw_meta_data.split('\n')
date_regex = (
    '<(Sat|Sun|Mon|Tue|Wed|Thu|Fri)., (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec). \\d{2}, \\d{4},\\s+\\d{2}:\\d{2} (AM|PM)>'
    )
for line in meta_lines:
if line.strip() == '':
if title_set == False:
date_match = re.search(date_regex, line)
full_contents = full_contents.strip()
if date_match:
title = full_contents.split('\n')[0]
datestamp_string = date_match.group(0)
date_stamp = None
first_line = full_contents[:150]
line = line.replace(datestamp_string, '').strip()
if ':' in line:
first_line = first_line.split('------------')[0]
date_stamp = datetime.datetime.strptime(datestamp_string,
    '<%a., %b. %d, %Y, %I:%M %p>')
key = line.split(':')[0]
key = '(no_key)'
self.entries.append(MetadataEntry('title', title, None))
value = ''.join(line.split(':')[1:]).strip()
value = line
if '|' in value:
if key == 'title':
items = value.split('|')
title_set = True
self.entries.append(MetadataEntry(key, value, date_stamp))
value = []
title = value
for item in items:
value.append(item.strip())

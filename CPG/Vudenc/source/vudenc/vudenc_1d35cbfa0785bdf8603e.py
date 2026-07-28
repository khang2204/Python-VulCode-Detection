@staticmethod...
total_parameters = 0
if keyword:
keyword_string = ("(jdk_entries.title LIKE '%" + keyword + "%' OR " +
    "jdk_entries.body LIKE '%" + keyword + "%') ")
keyword_string = ''
total_parameters += 1
if from_date:
from_date_string = "jdk_entries.date_last_modified >= '" + from_date + "' "
from_date_string = ''
total_parameters += 1
if to_date:
to_date_string = "jdk_entries.date_last_modified <= '" + to_date + "' "
to_date_string = ''
total_parameters += 1
sql = ('SELECT jdk_entries.id, jdk_entries.title ' + 'FROM jdk_entries ' +
    'WHERE ' + keyword_string + ('AND ' if keyword_string and (from_date or
    to_date) else '') + from_date_string + ('AND ' if from_date and to_date
     else '') + to_date_string + 'LIMIT 30;')
return db_execute(sql, True)

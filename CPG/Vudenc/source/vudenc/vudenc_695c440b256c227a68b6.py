def update_date(self, taskid, date=None):...
"""docstring"""
if not taskid.isdigit():
return Database.INVALID_ID
cur = self.__con.cursor()
if date == None:
date = 'NULL'
valid_date = Database.__format_date(date)
return Database.SUCCESS if cur.execute(
    'UPDATE tasks SET due_date=%s WHERE taskid=%s' % (date, int(taskid))
    ) else Database.DOES_NOT_EXIST
if valid_date == Database.INVALID_DATE:
return valid_date
date = "'%s'" % valid_date

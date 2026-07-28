def complete_task(self, taskid):...
"""docstring"""
if not taskid.isdigit():
return Database.INVALID_ID
cur = self.__con.cursor()
return Database.SUCCESS if cur.execute(
    'UPDATE tasks SET completed=TRUE WHERE taskid=%d' % int(taskid)
    ) else Database.DOES_NOT_EXIST

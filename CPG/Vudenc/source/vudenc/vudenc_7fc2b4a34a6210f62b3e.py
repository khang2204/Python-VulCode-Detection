def delete_task(self, taskid):...
"""docstring"""
if not taskid.isdigit():
return Database.INVALID_ID
cur = self.__con.cursor()
return Database.SUCCESS if cur.execute('DELETE FROM tasks WHERE taskid=%d' %
    int(taskid)) else Database.DOES_NOT_EXIST

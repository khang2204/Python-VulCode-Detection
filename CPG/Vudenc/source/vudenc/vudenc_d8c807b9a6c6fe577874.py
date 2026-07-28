@staticmethod...
_cursor = DBManager.conn()
result = _cursor.execute(sql)
return DBManager.error_handle()
if cursor:
return _cursor
return result

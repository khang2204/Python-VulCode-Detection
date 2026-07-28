def db_getMessagesFromDialog(dialogID):...
sql = (
    """SELECT user_id, content, created_at, section_id
FROM messages
WHERE dialog_id='%s'"""
     % dialogID)
return sql_execute(sql)

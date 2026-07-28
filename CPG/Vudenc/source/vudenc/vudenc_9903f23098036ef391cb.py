def db_addUserInDialog(userID, dialogID, permission):...
sql = (
    """INSERT INTO dialogUser (dialog_id, user_id, permission)
VALUES (%d, %d, %d)"""
     % dialogID, userID, permission)
return {'status': 1}

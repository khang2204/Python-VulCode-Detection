def db_addMessageForDialog(userID, content, dialogID, section_id=0):...
sql = (
    """INSERT INTO messages (dialog_id, content, created_at, user_id, section_id)
VALUES (%d, '%s', NOW(), %d, %d)"""
     % (dialogID, content, userID, section_id))
return {'status': 1}

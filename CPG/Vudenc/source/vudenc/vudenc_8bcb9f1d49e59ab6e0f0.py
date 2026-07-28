from modules.database import sql_execute
def db_addDialog(nameDialog):...
sql = ("""INSERT INTO dialogs (name, created_at)
VALUES ('%s', NOW())""" %
    nameDialog)
return {'status': 1}

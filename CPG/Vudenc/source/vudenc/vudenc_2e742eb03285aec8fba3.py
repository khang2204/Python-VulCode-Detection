def __init__(self):...
if DBConnection.con is None:
DBConnection.con = connection.cursor()
logger.error("""################## Erreur :
{0}""".format(db_error))
logger.info('################## Database connection opened.')

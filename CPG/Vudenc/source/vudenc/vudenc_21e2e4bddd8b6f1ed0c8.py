def __del__(self):...
if DBConnection.con is not None:
DBConnection.con.close()
logger.info('################## Database connection closed.')

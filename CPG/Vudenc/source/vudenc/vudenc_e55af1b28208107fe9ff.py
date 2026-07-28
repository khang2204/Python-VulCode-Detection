def __init__(self):...
self.conn = pymysql.connect(user=config.mysql_credentials['user'], password
    =config.mysql_credentials['password'], host=config.mysql_credentials[
    'host'], db=config.mysql_credentials['database'], cursorclass=pymysql.
    cursors.DictCursor)
self.cur = self.conn.cursor()

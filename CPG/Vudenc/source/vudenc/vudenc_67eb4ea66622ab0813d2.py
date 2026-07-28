def __init__(self, db):...
connection = pymysql.connect(host='localhost', user='root', password='', db
    =db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,
    autocommit=True)
self.connection = connection

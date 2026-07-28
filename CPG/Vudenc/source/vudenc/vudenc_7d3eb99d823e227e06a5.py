from modules import sql
def __init__(self, conn=None, name=None, password=None, email=None, country...
self.name = name
self.password = password
self.email = email
self.country = country
self.conn = conn
def clean(self):...
self.name = None
self.password = None
self.email = None
self.count = None
def userLogin(self):...
sqlName = (
    "select count(*) from users where name='%s' and                 password='%s';"
     % (self.name, self.password))
checkName = sql.queryDB(self.conn, sqlName)
result = checkName[0][0]
if result == 0:
self.clean()
return True
return False

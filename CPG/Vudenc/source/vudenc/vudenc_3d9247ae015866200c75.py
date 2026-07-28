import telebot
import sqlite3
def __init__(self, db_name):...
super(DbHandler, self).__init__()
self.db_name = db_name
def __db_connect__(self):...
self.db = sqlite3.connect(self.db_name)
self.db.row_factory = sqlite3.Row
self.cursor = self.db.cursor()
def __db_disconnect__(self):...
self.db.close()
def insert(self, table, values, updater=None):...
self.__db_connect__()
self.__db_disconnect__()
def select(self, table, where=None):...
if not updater:
return False
self.__db_connect__()
print(e)
def delete(self, table, where=None):...
updater = values
updater_str = ', '.join([(k + "='" + str(updater[k]) + "'") for k in
    updater.keys()])
if where:
self.__db_disconnect__()
self.__db_connect__()
print(e)
def __init__(self, telegram_id):...
values_str = ', '.join([("'" + str(values[k]) + "'") for k in values.keys()])
self.cursor.execute('SELECT * FROM ' + table + ' WHERE (' + where + ')')
self.cursor.execute('SELECT * FROM ' + table)
return False
if where:
self.__db_disconnect__()
super(Explorer, self).__init__()
columns_str = ', '.join([("'" + str(k) + "'") for k in values.keys()])
data = self.cursor.fetchall()
self.cursor.execute('DELETE FROM ' + table + ' WHERE (' + where + ')')
self.cursor.execute('DELETE FROM ' + table)
return False
self.user_id = db.select('user', 'telegram_id = ' + str(telegram_id))[0]['id']
where_str = 'AND '.join([(k + "='" + str(updater[k]) + "'") for k in
    updater.keys()])
self.__db_disconnect__()
self.db.commit()
self.path = [db.select('directory', 
    "name = '/' AND parent_directory_id = 'NULL' AND user_id = " + str(self
    .user_id))[0]['id']]
exists = len(self.cursor.execute('SELECT * FROM ' + table + ' WHERE (' +
    where_str + ')').fetchall())
return data
self.__db_disconnect__()
self.last_action_message_ids = []
if exists:
return True
def get_path_string(self):...
values_str = ', '.join([(k + "='" + str(values[k]) + "'") for k in values.
    keys()])
self.cursor.execute('INSERT INTO ' + table + '(' + columns_str +
    ') VALUES (' + values_str + ')')
if len(self.path) == 1:
self.cursor.execute('UPDATE ' + table + ' SET ' + values_str + ' WHERE ' +
    where_str)
self.db.commit()
return '/'
directory_ids_string = ', '.join([str(each) for each in self.path])
self.db.commit()
self.__db_disconnect__()
directories = db.select('directory', 'id in (' + directory_ids_string + ')')
self.__db_disconnect__()
return True
return '/'.join([directory['name'] for directory in directories])[1:]
return True

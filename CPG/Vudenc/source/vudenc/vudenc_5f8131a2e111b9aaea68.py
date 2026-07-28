def execute(self, command, **args):...
self._cur = self._db.cursor()
self._cur.execute(command, **args)
final_arr = None
self._db.commit()
final_arr = self._cur.fetchall()
self._cur.close()
return final_arr

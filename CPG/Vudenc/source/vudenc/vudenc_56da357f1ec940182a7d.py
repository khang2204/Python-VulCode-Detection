def show(self, tag=None):...
"""docstring"""
cur = self.__con.cursor(MySQLdb.cursors.DictCursor)
where_clause = "WHERE name='%s'" % tag if not tag == None else ''
cur.execute(
    'SELECT name, taskid, description, due_date, completed FROM tasks NATURAL JOIN tags %s ORDER BY tagid, taskid'
     % where_clause)
return cur.fetchall()

def select_recent(self):...
last = int(time()) - one_week
stmt = ('SELECT {} FROM {} WHERE timestamp >= {} ORDER BY timestamp DESC'.
    format(columns, tb_name, str(last)))
rows = self.connection.execute(stmt)
return rows

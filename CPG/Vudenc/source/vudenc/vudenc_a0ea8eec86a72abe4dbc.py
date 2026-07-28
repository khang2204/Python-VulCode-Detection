def insert_into_mysql_command(command_str):...
"""docstring"""
sql = text(str(command_str))
s.execute(sql)
s.commit()
